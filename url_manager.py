# -*- coding: utf-8 -*-


from threading import Lock


class LockedSet(set):
    """A set where add(), remove(), and 'in' operator are thread-safe"""
    def __init__(self, *args, **kwargs):
        self._lock = Lock()
        super(LockedSet, self).__init__(*args, **kwargs)

    def add(self, item):
        with self._lock:
            super(LockedSet, self).add(item)

    def remove(self, item):
        with self._lock:
            super(LockedSet, self).remove(item)

    def __contains__(self, item):
        with self._lock:
            super(LockedSet, self).__contains__(item)


class URLManager(object):
    """URL 管理器"""
    def __init__(self):
        self.new_urls = LockedSet()
        self.crawled_urls = LockedSet()

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
