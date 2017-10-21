import crawler_poi as cp

def get_fixed_bug_url():
    url = 'https://poi.apache.org/changes.html'
    url_dict = cp.get_fixed_bug_url(url)
    print(url_dict)

def test_get_patch_file_url():
    url = 'https://bz.apache.org/bugzilla/show_bug.cgi?id=61033'
    path_url = cp.get_patch_file_url(url)
    print(path_url)

def test_extract_bug_module_name():
    patch_url = 'https://bz.apache.org/bugzilla/attachment.cgi?id=34954'
    modules = cp.extract_bug_module_name(patch_url)
    print(modules)

# test_get_patch_file_url()
test_extract_bug_module_name()
