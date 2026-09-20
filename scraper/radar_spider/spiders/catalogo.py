import scrapy


class CatalogoSpider(scrapy.Spider):
    name = 'catalogo'
    allowed_domains = ['example.com']
    start_urls = ['https://example.com/']

    def parse(self, response):
        yield {'title': response.css('title::text').get(), 'url': response.url}
