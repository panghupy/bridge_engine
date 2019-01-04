# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BridgeItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    source = scrapy.Field()
    summary = scrapy.Field()
    time = scrapy.Field()
    keyword = scrapy.Field()

    def insert_data(self, dict):
        insert_sql = 'INSERT INTO news_news(%s) VALUES (%s)' % (
            ','.join(dict.keys()), ','.join(['%s'] * len(dict)))

        print('数据库插入语句',insert_sql)

        parmas = list(dict.values())

        return insert_sql, parmas
