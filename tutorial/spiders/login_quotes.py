import scrapy
from scrapy.http import FormRequest

from tutorial.items import TutorialItem



class LoginQuotesSpider(scrapy.Spider):
    name = "login"


    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/login'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
             'username':'clifton',
             'password':'clifton'
        },callback=self.start_scraping)

    def start_scraping(self, response):
        items = TutorialItem()
        all_quotes = response.css("div.quote")
        for quotes in all_quotes:
            title = quotes.css("span.text::text").extract()
            author = quotes.css(".author::text").extract()
            tag = quotes.css(".tag::text").extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            yield items

        # next_page = 'http://quotes.toscrape.com/page/{}/'.format((QuotesSpider.page_number))
        # if QuotesSpider.page_number <= 11:
        #     QuotesSpider.page_number += 1
        #     print("******************* : ", QuotesSpider.page_number)
        #     yield response.follow(next_page, callback=self.parse)


