# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging
import sqlite3
import pymongo
from itemadapter import ItemAdapter
# import json


class MongodbPipeline:
    def open_spider(self, spider):
        logging.info("Opening spider")
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client['scrapySectionDB']

        self.file = open('data.json', 'w')
    
    
    def close_spider(self, spider):
        logging.info("Closing spider")
        self.client.close()
        
        
    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item


class SQLitPipeline:
    def open_spider(self, spider):
        logging.info("Opening spider")
        self.connection = sqlite3.connect('scrapySection.db')
        self.c = self.connection.cursor()
        
        try:
            self.c.execute('''
                CREATE TABLE movies (
                    title TEXT,
                    plot TEXT,
                    transcript TEXT,
                    url TEXT
                )
            ''')
            self.connection.commit()
        except sqlite3.OperationalError:
            pass
    
    def close_spider(self, spider):
        logging.info("Closing spider")
        self.connection.close()
        
        
    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO movies (title, plot, transcript, url) VALUES(?,?,?,?)
        ''', (
            item.get('title'),
            item.get('plot'),
            item.get('transcript'),
            item.get('url')
        ))
        self.connection.commit()
        return item