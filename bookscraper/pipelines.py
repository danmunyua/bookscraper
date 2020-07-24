# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonItemExporter


class BookscraperPipeline:
    def process_item(self, item, spider):
        return item


class BookRatingPipeline(object):
    def process_item(self, item, spider):
        rating = str(item["rating"])
        if "one" in rating:
            item["rating"] = 1
        elif "two" in rating:
            item["rating"] = 2
        elif "three" in rating:
            item["rating"] = 3
        elif "four" in rating:
            item["rating"] = 4
        elif "five" in rating:
            item["rating"] = 5

        return item


class JsonPipeline(object):
    def __init__(self):
        self.file = open("books.json", "wb")
        self.exporter = JsonItemExporter(
            self.file, encoding="utf-8", ensure_ascii=False
        )
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
