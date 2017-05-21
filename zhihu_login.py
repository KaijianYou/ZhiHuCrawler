# -*- coding: utf-8 -*-


import re
import os.path
import time
import json
try:
    import http.cookiejar as cookielib
except:
    import cookielib
try:
    from urllib import urlencode
except:
    from urllib.parse import urlencode

import requests
try:
    from PIL import Image
except:
    pass

from settings import *


try:
    input = raw_input
except:
    pass


class ZhiHuLogin(object):
    """知乎登录"""
    def __init__(self, timeout=60):
        self._session = requests.session()
        self._session.headers.update(default_header)
        self._timeout = timeout

    def _load_cookies(self):
        """加载 Cookie"""
        # 从保存的 cookie 文件中加载 cookie
        self._session.cookies = cookielib.LWPCookieJar(filename='zhihu_cookies')
        try:
            self._session.cookies.load(ignore_discard=True)
        except Exception as e:
            print('无法加载 Cookie', e)

    def _get_xsrf(self):
        """获取动态变化的 _xsrf"""
        r = self._session.get(zhihu_url, timeout=self._timeout)
        if r.status_code != 200:
            return None
        page = r.text
        pattern = r'name="_xsrf" value="(.*?)"'
        _xsrf = re.findall(pattern, page)[0]
        return _xsrf

    def _get_captcha_pic(self):
        """获取验证码图片"""
        params = {
            'r': str(int(time.time() * 1000)),
            'type': 'login',
            'lang': 'cn',
        }
        url = captcha_url + '?' + urlencode(params)
        r = self._session.get(url, timeout=self._timeout)
        with open('captcha.jpg', 'wb') as f:
            f.write(r.content)
        # 使用 pillow 的 Image 打开图片
        try:
            img = Image.open('captcha.jpg')
            img.show()
            img.close()
        except Exception as e:
            print('请手动打开 "{0}" 并输入图片中倒立的文字'
                  .format(os.path.abspath('captcha.jpg')))
        captcha = input('请输入图片中倒立的文字：')
        return captcha

    def is_login(self):
        self._load_cookies()
        r = self._session.get(user_setting_url, allow_redirects=False)
        return True if r.status_code == 200 else False

    def login(self, account, password):
        """提供账号和密码进行登录"""
        xsrf = self._get_xsrf()
        default_header['X-Xsrftoken'] = xsrf
        default_header['X-Requested-With'] = 'XMLHttpRequest'  # Ajax 请求

        if re.match(r'^1\d{10}$', account):  # 账户名是手机号
            print('手机号登录')
            login_url = phonenum_login_url
            data = {
                'password': password,
                'phone_num': account,
                '_xsrf': xsrf,
            }
        elif '@' in account:  # 账户名是邮箱号
            print('邮箱登录')
            login_url = email_login_url
            data = {
                'email': account,
                'password': password,
                '_xsrf': xsrf,
            }
        else:
            print('账号有误，请重新登录')
            return

        r = self._session.post(login_url, data=data, timeout=self._timeout)
        # 直接登录失败，需要输入验证码才能登录
        if r.json()['r'] == 1:
            data['captcha'] = self._get_captcha_pic()
            r = self._session.post(login_url, timeout=self._timeout)
            print(r.json()['msg'])

        self._session.cookies.save()  # 保存 cookie 到文件


if __name__ == '__main__':
    zhl = ZhiHuLogin()
    if zhl.is_login():
        print('已经登录')
    else:
        account = input('请输入用户名：')
        password = input('请输入密码：')
        zhl.login(account, password)
