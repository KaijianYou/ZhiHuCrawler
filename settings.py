# -*- coding: utf-8 -*-


import sys
import logging


# 默认 Request 首部信息
default_header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Host': 'www.zhihu.com',
    'Referer': 'https://www.zhihu.com/',
    'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'),
}

zhihu_url = 'https://www.zhihu.com'
user_url_prefix = zhihu_url + '/people'
user_setting_url = zhihu_url + '/settings/profile'
email_login_url = zhihu_url + '/login/email'
phonenum_login_url = zhihu_url + '/login/phone_num'
captcha_url = zhihu_url + '/captcha.gif'


log_file = 'crawl.log'
logging.root.setLevel(level=logging.INFO)
logger = logging.getLogger('crawl')
log_fmt = logging.Formatter('%(asctime)s: [%(levelname)s] %(message)s')
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(log_fmt)
logger.addHandler(stream_handler)
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(log_fmt)
logger.addHandler(file_handler)
