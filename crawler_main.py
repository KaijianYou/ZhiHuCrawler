# -*- coding: utf-8 -*-


import url_manager
import html_downloader
import outputer
import html_parser


class CrawlerMain(object):
    """爬虫调度器"""
    def __init__(self):
        self._url_manager = url_manager.URLManager()  # URL 管理器
        self._downloader = html_downloader.HTMLDownloader()  # 下载器
        self._parser = html_parser.HTMLParser()  # 网页解析器
        self._outputer = outputer.Outputer()  # 输出器
        self._max_size = 1   # 爬取的最大用户数

    def crawl(self, root_url, max_size):
        self.max_size = max_size
        count = 1
        self._url_manager.add_url(root_url)
        while self._url_manager.has_next():
            try:
                next_url = self._url_manager.get_next()
                print('crawl {0}: {1}'.format(count, next_url))
                html_page = self._downloader.download(next_url)
                next_urls, data = self._parser.parse(next_url, html_page)
                self._url_manager.add_urls(next_urls)
                self._outputer.collect_data(data)

                count += 1
                if count > max_size:
                    break
            except Exception as e:
                print('Crawl failed\nError: {0}'.format(e))
        self._outputer.output_html()
        self._outputer.output_json()
        self._outputer.data_profiler()


if __name__ == '__main__':
    crawler = CrawlerMain()
    root_url = 'https://www.zhihu.com/people/tian-yu-bai/following'
    crawler.crawl(root_url, 10000)
