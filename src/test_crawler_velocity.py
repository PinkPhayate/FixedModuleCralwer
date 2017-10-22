import crawler_velocity as cv

def test_get_fixed_bug_url():
    url = 'http://velocity.apache.org/engine/2.0/changes.html'
    url_dict = cv.get_fixed_bug_url(url)
    print(url_dict)

def test_get_patch_file_url():
    url = 'https://issues.apache.org/jira/browse/VELOCITY-785'
    path_url = cv.get_patch_file_url(url)
    print(path_url)

def test_extract_bug_module_name():
    patch_url = 'https://bz.apache.org/bugzilla/attachment.cgi?id=34954'
    modules = cp.extract_bug_module_name(patch_url)
    print(modules)

# test_get_fixed_bug_url()
test_get_patch_file_url()
# test_extract_bug_module_name()
