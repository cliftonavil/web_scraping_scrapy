import scrapy
from ..items import  AmazonItem


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    page_number = 2

    def start_requests(self):
        urls = [
            'https://www.amazon.in/s?k=Mobile&ref=nb_sb_noss'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = AmazonItem()
        for mobile in response.css(".s-latency-cf-section"):
            title = mobile.css('.a-color-base.a-text-normal::text').extract()
            price = mobile.css(".a-price-whole::text").extract()
            delivery_on = mobile.css(".s-align-children-center .a-text-bold::text").extract()
            image_link = mobile.css(".s-image").xpath("@src").extract()

            print("title : ",title)

            items['title'] = title
            items['delivery_on'] = delivery_on
            items['price'] = price
            items['image_link'] = image_link
            yield items

        # next_page = 'https://www.amazon.in/s?k=Mobile&page={}&ref=sr_pg_{}'.format(AmazonSpider.page_number,AmazonSpider.page_number)
        next_page = 'https://www.amazon.in/s?k=Mobile&page={}&qid=1999999991&ref=sr_pg_{}'.format(AmazonSpider.page_number,AmazonSpider.page_number)
        if AmazonSpider.page_number <= 20:
            AmazonSpider.page_number+=1
            print("******************* : ", AmazonSpider.page_number)
            yield response.follow(next_page,callback=self.parse)

