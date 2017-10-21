import crawler_poi as cp

def main():
    url = 'https://poi.apache.org/changes.html'
    url_dict = cp.get_fixed_bug_url(url)
    cp.crawl_versions(url_dict)


if __name__ == '__main__':
    main()
