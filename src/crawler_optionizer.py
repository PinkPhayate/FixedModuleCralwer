import crawler_derby as cd

def skip_version(url_json, skip_versions):
    popped_url_json = url_json.copy()
    for version in url_json.keys():
        if version in skip_versions:
            del popped_url_json[version]
    return popped_url_json

def test_skip_version():
    skip_versions = ['10.10.2.0', '10.2.1.6', '10.5.3.0', '10.9.1.0', '10.7.1.1',
                     '10.12.1.1', '10.11.1.1', '10.4.1.3', '10.1.2.1', '10.8.3.0']

    url = 'http://db.apache.org/derby/derby_downloads.html'
    url_dict = cd.get_fixed_bug_url(url)
    url_dict = skip_version(url_dict, skip_versions=skip_versions)
    print(url_dict.keys())

if __name__ == '__main__':
    test_skip_version()
