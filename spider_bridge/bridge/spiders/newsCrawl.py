# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import BridgeItem


class NewscrawlSpider(CrawlSpider):
    name = 'newsCrawl'
    allowed_domains = ['baidu.com']
    key_words = ['建筑', '工程', '桥梁', '施工', '隧道']
    url_encode_words = ['%E5%BB%BA%E7%AD%91', '%E5%B7%A5%E7%A8%8B', '%E6%A1%A5%E6%A2%81', '%E6%96%BD%E5%B7%A5',
                        '%E9%9A%A7%E9%81%93']
    start_urls = ['http://news.baidu.com/ns?word=建筑&pn=20&cl=2&ct=1&tn=news&rn=20&ie=utf-8&bt=0&et=0',
                  'http://news.baidu.com/ns?word=工程&pn=20&cl=2&ct=1&tn=news&rn=20&ie=utf-8&bt=0&et=0',
                  'http://news.baidu.com/ns?word=桥梁&pn=20&cl=2&ct=1&tn=news&rn=20&ie=utf-8&bt=0&et=0',
                  'http://news.baidu.com/ns?word=施工&pn=20&cl=2&ct=1&tn=news&rn=20&ie=utf-8&bt=0&et=0',
                  'http://news.baidu.com/ns?word=隧道&pn=20&cl=2&ct=1&tn=news&rn=20&ie=utf-8&bt=0&et=0']

    rules = (
        Rule(LinkExtractor(allow=r'pn=\d+.*?0$', restrict_xpaths=('//p[@id="page"]//a')), callback='parse_item',
             follow=True),
    )

    def parse_item(self, response):

        news_list = response.xpath('//div[@class="result"]')
        for news in news_list:
            item = BridgeItem()
            item['title'] = ''.join(news.xpath('./h3/a/text()').extract()).replace('\n', '').strip()
            # print('文章标题:\t' + title)
            item['url'] = news.xpath('./h3/a/@href').extract_first()
            # print('文章链接：\t', url)
            source_item = news.xpath(
                './/div[contains(@class,"c-summary c-row")]//p[@class="c-author"]/text()').extract()
            item['source'] = ''.join(source_item).replace('\t', '').replace('\n', '').strip().split('\xa0\xa0')[0]
            item['time'] = ''.join(source_item).replace('\t', '').replace('\n', '').strip().split('\xa0\xa0')[1]
            # print('文章来源:\t' + source)
            # print('发表时间:\t' + time)
            # 判断是否有缩略图
            if not news.xpath('.//div[@class="c-span6"]'):
                data = news.xpath('.//div[contains(@class,"c-summary c-row")]/text()').extract()
            else:
                data = news.xpath('.//div[@class="c-span18 c-span-last"]/text()').extract()
            item['summary'] = ''.join(data).replace('\n', '').replace(' ','')
            # print('文章摘要：\t' + Summary)
            pattern = re.compile('.*?http://news.baidu.com/ns\?word=(.*?)&pn=\d+.*?')
            key_word = re.findall(pattern=pattern, string=response.url)[0]
            key = self.key_words[self.url_encode_words.index(key_word)]
            item['keyword'] = key
            # print(item)
            yield item
