import crawler_log4j as cl

def test_get_fixed_bug_url():
    url = 'https://logging.apache.org/log4j/2.x/changes-report.html#a2.9.1'
    url_dict = cl.get_fixed_bug_url(url)
    print(url_dict)

def test_get_patch_file_url():
    url = 'https://issues.apache.org/jira/browse/LOG4J2-51'
    path_url = cl.get_patch_file_url(url)
    print(path_url)

def test_extract_bug_module_name():
    patch_url = 'https://issues.apache.org/jira/secure/attachment/12458997/velocity-785.patch'
    modules = cl.extract_bug_module_name(patch_url)
    print(modules)

test_get_fixed_bug_url()
# test_get_patch_file_url()
# test_extract_bug_module_name()
