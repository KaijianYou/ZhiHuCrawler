# -*- coding: utf-8 -*-

try:
    import html
except ImportError as e:
    from HTMLParser import HTMLParser
    html = HTMLParser()

import requests


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookies': '',
    'Host': 'www.zhihu.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.zhihu.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}

timeout = 120


class HTMLDownloader(object):
    def __init__(self):
        pass

    def download(self, url):
        if url is None:
            return None

        r = requests.get(url, headers=headers, timeout=timeout)
        if r.status_code != 200:
            return None

        if r.encoding == 'ISO-8859-1':
            encodings = requests.utils.get_encodings_from_content(
                str(r.content))
            if encodings:
                r.encoding = encodings[0]
            else:
                r.encoding = r.apparent_encoding
            r._content = r.content.decode(r.encoding).encode('utf8')

        page = html.unescape(r.text)
        return page


if __name__ == '__main__':
    pass
