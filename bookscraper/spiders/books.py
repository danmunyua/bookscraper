# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst
from scrapy.spiders import CrawlSpider, Rule
from w3lib.html import remove_tags

from bookscraper.items import BookscraperItem


class BooksSpider(CrawlSpider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    rules = (
        Rule(LinkExtractor(restrict_css=".pager .next > a"), follow=True),
        Rule(
            LinkExtractor(restrict_css=".product_pod > h3 > a"), callback="parse_item"
        ),
    )

    def parse_item(self, response):
        book_loader = ItemLoader(item=BookscraperItem(), response=response)
        book_loader.default_input_processor = MapCompose(remove_tags)
        book_loader.default_output_processor = TakeFirst()

        book_loader.add_css("title", ".product_main > h1")
        book_loader.add_css("price", ".product_main .price_color")
        book_loader.add_css("upc", ".table.table-striped > tr:nth-child(1) > td")
        book_loader.add_css(
            "product_type", ".table.table-striped > tr:nth-child(2) > td"
        )
        book_loader.add_css("tax", ".table.table-striped > tr:nth-child(5) > td")
        book_loader.add_css("stock", ".table.table-striped > tr:nth-child(6) > td")
        book_loader.add_css("reviews", ".table.table-striped > tr:nth-child(7) > td")
        book_loader.add_css("rating", ".product_main p.star-rating::attr(class)")

        yield book_loader.load_item()
