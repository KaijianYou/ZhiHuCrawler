# -*- coding: utf-8 -*-


class URLManager(object):
    def __init__(self):
        self.new_urls = set()
        self.crawled_urls = set()

    def add_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.crawled_urls:
            self.new_urls.add(url)

    def add_urls(self, urls):
        if not urls:
            return
        for url in urls:
            self.add_url(url)

    def has_next(self):
        return len(self.new_urls) != 0

    def get_next(self):
        url = self.new_urls.pop()
        self.crawled_urls.add(url)
        return url


if __name__ == '__main__':
    pass
