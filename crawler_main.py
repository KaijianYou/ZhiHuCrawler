# -*- coding: utf-8 -*-


import url_manager
import html_downloader
import outputer
import html_parser


class CrawlerMain(object):
    def __init__(self):
        self.url_manager = url_manager.URLManager()  # URL 管理器
        self.downloader = html_downloader.HTMLDownloader()  # 下载器
        self.parser = html_parser.HTMLParser()  # 网页解析器
        self.outputer = outputer.Outputer()  # 输出器
        self.max_size = 1   # 爬取的最大用户数

    def crawl(self, root_url, max_size):
        self.max_size = max_size
        count = 1
        self.url_manager.add_url(root_url)
        while self.url_manager.has_next():
            try:
                next_url = self.url_manager.get_next()
                print('crawl {0}: {1}'.format(count, next_url))
                html_page = self.downloader.download(next_url)
                next_urls, data = self.parser.parse(next_url, html_page)
                self.url_manager.add_urls(next_urls)
                self.outputer.collect_data(data)

                count += 1
                if count > max_size:
                    break
            except Exception as e:
                print('Crawl failed\nError: {0}'.format(e))
        self.outputer.output_html()
        self.outputer.output_json()
        self.outputer.data_profiler()


if __name__ == '__main__':
    crawler = CrawlerMain()
    root_url = 'https://www.zhihu.com/people/tian-yu-bai/following'
    crawler.crawl(root_url, 1000)
