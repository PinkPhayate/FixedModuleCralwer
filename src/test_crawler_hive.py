import crawler_hive as ch

def test_get_fixed_bug_url():
    url = 'https://hive.apache.org/downloads.html'
    url_dict = ch.get_fixed_bug_url(url)
    print(url_dict)

def test_get_fixed_report_url():
    url = "https://issues.apache.org/jira/secure/ReleaseNote.jspa?version=12320745&styleName=Text&projectId=12310843"
    link = ch.get_fixed_report_url(url)
    print(link)

def test_get_patch_file_url():
    # url = 'https://bz.apache.org/bugzilla/show_bug.cgi?id=61033'
    url = 'https://issues.apache.org/jira/browse/HIVE-14014'
    path_url = ch.get_patch_file_url(url)
    print(path_url)

def test_extract_bug_module_name():
    patch_url = 'https://issues.apache.org/jira/secure/attachment/12742245/workingPatch.patch'
    modules = ch.extract_bug_module_name(patch_url)
    print(modules)

def test_crawl_versions():
    url_dict = {}
    url_dict['1.2.2'] = ['/jira/secure/attachment/12810680/HIVE-14014.01.patch', '/jira/secure/attachment/12810695/HIVE-14014.02.patch', '/jira/secure/attachment/12811172/HIVE-14014.03.patch', '/jira/secure/attachment/12811756/HIVE-14014.04.patch']
    ch.crawl_versions(url_dict)

def test_find_bug_module():
    url = "https://issues.apache.org/jira/browse/HIVE-17705"
    list = ch.find_bug_module(url)
    print(list)


# test_get_fixed_bug_url()
# test_get_fixed_report_url()
# test_get_patch_file_url()
# test_extract_bug_module_name()
# test_crawl_versions()
# url = 'https://issues.apache.org/jira/browse/HIVE-13556'
# from urllib import request
# source = request.urlopen(url)
# print(source)
test_find_bug_module()
