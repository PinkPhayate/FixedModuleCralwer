import crawler_hive as ch
from logging import getLogger
import sys
args = sys.argv
LOG_DIR = args[1] if 1 < len(args) else ''

def main():
    url = 'https://hive.apache.org/downloads.html'
    url_dict = ch.get_fixed_bug_url(url)
    ch.crawl_versions(url_dict)

def config_logger():
    import logging
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)

    error_logger = logging.getLogger("error_log")
    # error_logger.addHandler(sh)
    error_logger.setLevel(logging.ERROR)
    fh = logging.FileHandler(filename=LOG_DIR+"error_hive.log")
    fh.setFormatter(formatter)
    error_logger.addHandler(fh)

    report_logger = logging.getLogger("report_log")
    report_logger.addHandler(sh)
    report_logger.setLevel(logging.INFO)
    fh = logging.FileHandler(filename=LOG_DIR+"report_hive.log")
    fh.setFormatter(formatter)
    report_logger.addHandler(fh)

if __name__ == '__main__':
    config_logger()
    main()
