import scrapy
from ..items import TutorialItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    page_number = 2

    def start_requests(self):
        urls = [
            # 'http://quotes.toscrape.com/'
            'http://quotes.toscrape.com/page/1/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
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

        next_page = 'http://quotes.toscrape.com/page/{}/'.format((QuotesSpider.page_number))
        if QuotesSpider.page_number <= 11:
            QuotesSpider.page_number+=1
            print("******************* : ", QuotesSpider.page_number)
            yield response.follow(next_page,callback=self.parse)

        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     print("******************* : ",next_page)
        #     yield response.follow(next_page,callback=self.parse)

# response.xpath("//span[@class='text']/text()").extract()
# response.xpath("//span[@id='text']/text()").extract()

# response.css("li.next a").xpath("@href").extract()
# response.css("span").xpath("@aria-label").extract()
# response.css(".user-details").xpath("@href").extract()

# response.css("a").xpath("@href").extract()  // All links



# response.xpath("//div[@class='grid--cell fw-bold']/text()").extract()