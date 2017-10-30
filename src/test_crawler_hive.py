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
    url = 'https://issues.apache.org/jira/browse/HIVE-12492'
    path_url = ch.get_patch_file_url(url)
    print(path_url)

def test_extract_bug_module_name():
    patch_url = 'https://issues.apache.org/jira/secure/attachment/12742245/workingPatch.patch'
    modules = ch.extract_bug_module_name(patch_url)
    print(modules)

# test_get_fixed_bug_url()
# test_get_fixed_report_url()
test_get_patch_file_url()
# test_extract_bug_module_name()
