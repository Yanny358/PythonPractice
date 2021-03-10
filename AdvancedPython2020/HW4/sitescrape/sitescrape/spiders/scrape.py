import scrapy


class SiteScrape(scrapy.Spider):
    name = "computers_spider"
    start_urls = ['https://www.osta.ee/en/category/computers']

    def parse(self, response):
        SET_SELECTOR = '.offer-thumb__article'
        for computer in response.css(SET_SELECTOR):
            TITLE_SELECTOR = './/p[@class= "offer-thumb__title"]/a/text()'
            PRICE_SELECTOR = './/span[@class= "price-bn price-cp"]/text()'
            PICTURE_SELECTOR = './/img[@class= "lazy"]/@src'
            yield {
                'Title': computer.xpath(TITLE_SELECTOR).extract_first(),
                'Price': computer.xpath(PRICE_SELECTOR).extract_first(),
                'Picture href': computer.xpath(PICTURE_SELECTOR).extract_first(),
            }
        NEXT_PAGE_SELECTOR = '.page-selector d-none d-sm-block a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
