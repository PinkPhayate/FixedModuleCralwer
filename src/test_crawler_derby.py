import crawler_derby as cd

def test_get_fixed_bug_url():
    url = 'http://db.apache.org/derby/derby_downloads.html'
    url_dict = cd.get_fixed_bug_url(url)
    print(url_dict)

def test__get_fixed_report_url():
    url = 'http://db.apache.org/derby/releases/release-10.1.3.1.html'
    link = cd.get_fixed_report_url(url)
    print(link)
def test_get_patch_file_url():
    url = 'https://bz.apache.org/bugzilla/show_bug.cgi?id=61033'
    url = 'https://issues.apache.org/jira/browse/DERBY-6783'
    path_url = cd.get_patch_file_url(url)
    print(path_url)

def test_extract_bug_module_name():
    patch_url = 'https://issues.apache.org/jira/secure/attachment/12742245/workingPatch.patch'
    modules = cd.extract_bug_module_name(patch_url)
    print(modules)

# test_get_fixed_bug_url()
test__get_fixed_report_url()
# test_get_patch_file_url()
# test_extract_bug_module_name()
