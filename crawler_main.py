# -*- coding: utf-8 -*-


from time import time

import html_downloader
import html_parser
import outputer
import url_manager
from settings import user_url_prefix


class CrawlerMain(object):
    """爬虫调度器"""
    def __init__(self):
        self._url_manager = url_manager.URLManager()  # URL 管理器
        self._downloader = html_downloader.HTMLDownloader()  # HTML 下载器
        self._parser = html_parser.HTMLParser()  # HTML 解析器
        self._outputer = outputer.Outputer()  # 数据采集、输出器

    def crawl(self, root_url, max_size=1000):
        count = 1
        self._url_manager.add_url(root_url)
        try:
            while self._url_manager.has_next():
                next_url = self._url_manager.get_next()
                html_page = self._downloader.download(next_url)
                print('crawl {0}: {1}'.format(count, next_url))
                next_urls, data = self._parser.parse(next_url, html_page)
                self._url_manager.add_urls(next_urls)
                self._outputer.collect_data(data)

                count += 1
                if count > max_size:
                    break
        except Exception as e:
            print('Crawl failed\nError: {error}'.format(error=e))
        finally:
            self._outputer.output_html()
            self._outputer.output_json()
            self._outputer.data_profiler()


if __name__ == '__main__':
    crawler = CrawlerMain()
    root_url = user_url_prefix + '/tian-yu-bai/following'
    start_time = time()
    crawler.crawl(root_url, 100)
    end_time = time()
    print(end_time - start_time)
