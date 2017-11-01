import lxml
from bs4 import BeautifulSoup
import sys
from urllib import request
from multiprocessing import Process
from tqdm import tqdm
from logging import getLogger
error_logger = getLogger("error_log_hive")
report_logger = getLogger("report_log_hive")

PATCH_DOMAIN_URL = 'https://issues.apache.org'
MODULE_POST_STRING = '.java'
RELEASE_NOTE_URL = 'https://issues.apache.org'
METRICS_DIR = ''

def export_bug_modules(version, module_set):
    filename = METRICS_DIR + 'hive_{}_bgmd.csv'.format(version)
    with open(filename, mode='w', encoding='utf-8') as fh:
        for module in module_set:
            fh.write('{}\n'.format(module))


def get_fixed_report_url(url):
    source = request.urlopen(url)
    soup = BeautifulSoup(source, "lxml")
    url_list = []
    for h2 in soup.findAll('h2'):
        if h2.text == 'Bug':
            ul = h2.find_next_sibling()
            for a in ul.findAll('a'):
                link = a.attrs['href']
                url_list.append(link)
    return url_list

def get_fixed_bug_url(url):

    source = request.urlopen(url)
    soup = BeautifulSoup(source, "lxml")
    versions = []
    links = []

    for a in soup.findAll("a"):
        if a.text == 'JIRA change log for this release':
            link = a.attrs['href']
            links.append(link)
            version_text = a.parent.find_previous_sibling('h3')
            versions.append(version_text.text.split(' ')[5])
    report_logger.info('version size: {}'.format(len(versions)))
    versions = versions[:7]     # 最初の方のバージョンは取り除いた

    url_dict = {}
    version_idx = 0
    for link, version in zip(links, versions):
        url_list = get_fixed_report_url(link)
        url_dict[version] = url_list
        version_idx += 1
    return url_dict

def get_patch_file_url(url):
    source = request.urlopen(url)
    soup = BeautifulSoup(source, "lxml")
    patch_urls = []
    for div in soup.findAll("div", attrs={'class': 'attachment-thumb'}):
        link = div.find('a').attrs['href']
        patch_urls.append(link)
    return patch_urls

def extract_bug_module_name(patch_url):
    def __is_modified_line(line):
        if len(line) < 3:
            return False
        line = line.decode('utf-8')
        prim_string = line[:3]
        if prim_string != '---':
            return False
        if MODULE_POST_STRING not in line:
            return False
        return True

    def __extract_module_name(line):
        module_name = line.split(' ')[1]
        return module_name.rsplit(MODULE_POST_STRING)[0] + MODULE_POST_STRING

    source = request.urlopen(patch_url)
    lines = source.readlines()
    modules = []
    for idx, line in enumerate(lines):
        try:
            if __is_modified_line(line):
                module_name = __extract_module_name(line.decode('utf-8'))
                modules.append(module_name)
        except Exception:
            lines = []
            lines.append('this line couldnt convert unicode')
            lines.append('patch_url: {}, line: {}'.format(patch_url, idx))
            lines.append('file content: {}'.format(line))
            error_logger.error(lines)
    return modules

def find_bug_module(url):
    bug_module_map = []
    try:
        patch_urls = get_patch_file_url(url)
        patch_urls = filter(lambda x: x.split('.')[-1]=='patch', patch_urls)
    except:
        error_logger.error('this bug report couldnt be read patch files, url: {}'
                           .format(url))
        return []
    for patch_url in list(patch_urls):
        patch_url = '{}{}'.format(PATCH_DOMAIN_URL, patch_url)
        try:
            modules = extract_bug_module_name(patch_url)
            bug_module_map.extend(modules)
        except:
            error_logger.error('this patch file could not open: {}'
                               .format(patch_url))

    return list(set(bug_module_map))

def crawl_versions(url_json):
    report_logger.info('versions: {}'.format(url_json.keys()))
    jobs = []
    for version, url_array in url_json.items():
        modules = []
        report_logger.info('start to extract fixed module of {} '.format(version))
        url_array = map(lambda x: RELEASE_NOTE_URL + x, url_array)
        url_array = list(url_array)
        for url in tqdm(url_array):
            module_set = find_bug_module(url)
            modules.extend(module_set)
        log_msg = 'version: {} num of extracted module:  {}/{} '\
            .format(version, len(modules), len(url_array))
        report_logger.info(log_msg)
        job = Process(target=export_bug_modules, args=(version, modules))
        jobs.append(job)
        job.start()
    [job.join() for job in jobs]
