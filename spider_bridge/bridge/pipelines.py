# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi

import pymysql


# 异步插入数据库,有bug,先使用同步插入
class DBridgePipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        # 数据库的连接参数
        parmas = dict(
            host=settings['MYSQL_HOST'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PWD'],
            db=settings['MYSQL_DB'],
            port=settings['MYSQL_PORT'],
            charset='utf-8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True
        )
        print(parmas)
        # 一个*表示元组，**表示字典
        # 这里创建了一个连接池
        dbpool = adbapi.ConnectionPool('pymysql', **parmas)
        return cls(dbpool)

    def process_item(self, item, spider):
        # 让连接池执行数据插入任务，并传递参数
        print('进入管道')
        query = self.dbpool.runInteraction(
            self.insert_data_to_db,
            item,
        )
        # 添加一个数据插入失败的回调
        query.addErrback(self.handle_err, item)
        return item

    def insert_data_to_db(self, cursor, item):
        # 使用游标执行数据插入
        print('正在插入数据')
        insert_sql, parmas = item.insert_data(dict(item))
        print('数据库插入语句', insert_sql)
        cursor.execute(insert_sql, parmas)

    def handle_err(self, failure, item):
        # 数据插入失败的回调函数
        print(failure)
        print('数据库插入失败')


# 同步插入数据库
class BridgePipeline(object):
    #     将数据存储值mysql数据库
    #     _mysql_exceptions.OperationalError: (1366, 是因为数据库中的字符集与charset="utf8"不符合
    def __init__(self):
        self.conn = pymysql.Connect('localhost', 'root', '123456', 'bridge', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql, parmas = item.insert_data(dict(item))
        self.cursor.execute(insert_sql, parmas)
        self.conn.commit()
