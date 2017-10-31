import crawler_derby as cd
import crawler_optionizer as co
from logging import getLogger
import sys
args = sys.argv
LOG_DIR = args[1] if 1 < len(args) else ''
skip_versions = ['10.10.2.0', '10.2.1.6', '10.5.3.0', '10.9.1.0', '10.7.1.1',
                 '10.12.1.1', '10.11.1.1', '10.4.1.3', '10.1.2.1', '10.8.3.0',
                 '10.5.1.1']

def main():
    url = 'http://db.apache.org/derby/derby_downloads.html'
    url_dict = cd.get_fixed_bug_url(url)
    url_dict = co.skip_version(url_dict, skip_versions=skip_versions)
    cd.crawl_versions(url_dict)

def config_logger():
    import logging
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)

    error_logger = logging.getLogger("error_log")
    # error_logger.addHandler(sh)
    error_logger.setLevel(logging.ERROR)
    fh = logging.FileHandler(filename=LOG_DIR+"error_derby.log")
    fh.setFormatter(formatter)
    error_logger.addHandler(fh)

    report_logger = logging.getLogger("report_log")
    report_logger.addHandler(sh)
    report_logger.setLevel(logging.INFO)
    fh = logging.FileHandler(filename=LOG_DIR+"report_derby.log")
    fh.setFormatter(formatter)
    report_logger.addHandler(fh)

if __name__ == '__main__':
    config_logger()
    main()
