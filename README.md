# bookscraper
This is a Scrapy project to scrape information about books at [Books to Scrape](http://books.toscrape.com/)

## Extracted data

This project extracts all data including title, price, product type etc...
A sample item:
```
{
    'title': 'A Light in the Attic',
    'upc': '£51.77',
    'product_type': 'Books',
    'price': '£51.77',
    'tax': '£0.00',
    'stock': 'In stock (22 available)',
    'reviews': '0',
    'rating': '3'
}
```
## Spiders

This project contains 1 spider: books implemented with css selectors.
You can learn more about web scraping with Scrapy by going through the [Scrapy docs](https://doc.scrapy.org/en/latest/intro/tutorial.html) or
[Scrapy Tutorial](https://www.scrapingauthority.com/tutorials/scrapy/).

## Pipelines

`BookRatingPipeline` processes the "rating" field
`JsonPipeline` create json file
`CsvPipeline` process items field with comma and create csv file
You can disable pipelines in settings.py.

## Running Spiders

You can run a spider using the **scrapy crawl** command:

```
$ scrapy crawl books
```
