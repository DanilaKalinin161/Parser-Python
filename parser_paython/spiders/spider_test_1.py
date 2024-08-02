import scrapy


class SpiderTest1Spider(scrapy.Spider):
    name = "spider_test_1"
    allowed_domains = ["timeout.com"]
    start_urls = ["https://www.kinoafisha.info/rating/movies/"]

    def parse(self, response):
        for link in response.css('a.movieItem_title::attr(href)'):
            yield response.follow(link, callback=self.parse_film)
        for i in range(1, 10):
            next_page = f'https://www.kinoafisha.info/rating/movies/?page={i}/'
            yield response.follow(next_page, callback=self.parse)

    def parse_film(self, response):
        yield {
            'title': response.css('span.trailer_subtitle::text').get(),
            'rating': response.css('span.rating_num::text').get(),
            'year': response.css('span.trailer_year::text').get().split()[0],
        }


