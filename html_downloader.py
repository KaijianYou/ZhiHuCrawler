# -*- coding: utf-8 -*-

try:
    import html
except ImportError as e:
    from HTMLParser import HTMLParser
    html = HTMLParser()
try:
    import http.cookiejar as cookielib
except ImportError as e:
    import cookielib

import requests

from zhihu_login import ZhiHuLogin
from settings import default_header


class HTMLDownloader(object):
    """HTML 下载器"""
    def __init__(self):
        self._session = requests.Session()
        self._session.headers.update(default_header)
        self._session.adapters.DEFAULT_RETRIES = 5  # 请求重发最大次数限制
        # 登录知乎，获取 Cookie
        self._login = ZhiHuLogin()
        if not self._login.is_login():
            account = input('请输入用户名：')
            password = input('请输入密码：')
            self._login.login(account, password)

    def download(self, url, timeout=60):
        if url is None:
            return None

        r = self._session.get(url, timeout=timeout)
        if r.status_code != 200:
            return None

        # 获取正确的页面编码
        if r.encoding == 'ISO-8859-1':
            encodings = requests.utils.get_encodings_from_content(str(r.content))
            if encodings:
                r.encoding = encodings[0]
            else:
                r.encoding = r.apparent_encoding
            r._content = r.content.decode(r.encoding).encode('utf8')

        page = html.unescape(r.text)
        return page


if __name__ == '__main__':
    pass
