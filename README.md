# Python 爬虫练习
一个简单的单线程爬虫，通过爬取知乎用户的 "关注" 页面来获取部分用户的信息。

还有一些地方需要完善(。・`ω´・)

* crawler_main  调度器
* url_manager url  管理器
* html_downloader html 下载器
* html_parser html 网页解析器
* outputer 数据采集、输出器
* zhihu_login  知乎登录

# 运行环境
python 2.7 和 Python 3（优先）

# 依赖库
* BeautifulSoup 4
* Requests
* Pillow

### 安装依赖库
    pip install beautifulsoup
    pip install requests
    pip install pillow

# 运行
首先你需要有个知乎账号。

### 获取 Cookie
* 自动获取<br/>
    默认使用的方法。在程序运行时输入账号和密码，程序会尝试登录知乎，登录成功后即会获取 cookie，并保存到文件中留待下次使用。

* 手动获取<br/>
    首先在浏览器中用账号登录知乎，然后在浏览器的开发工具中获取 HTTP 首部信息的 "Cookie" 字段，复制这个字段的值，并黏贴到 "headers" 字典（在 html_downloader.py 中）中的 "Cookies"。
    ```
    headers = {
        'Cookies': '此处填入 cookie'，
    }
    ```

### 启动
    python crawler_main.py

* 若自动获取 Cookie 失败，可试试手动获取 Cookie 的方法。
* 若页面解析错误，可能是知乎页面被修改了，这时需要根据实际情况改写网页解析器中的爬取规则。

# 参考
1. [Python开发简单爬虫](http://www.imooc.com/learn/563)<br/>
2. [使用BeautifulSoup爬虫(以知乎为例)](http://mingxinglai.com/cn/2016/08/crawl-with-bs/)<br/>
3. [知乎登录](https://github.com/xchaoinfo/fuck-login/blob/master/001%20zhihu/zhihu.py)<br/>