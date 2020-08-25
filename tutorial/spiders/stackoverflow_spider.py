import scrapy

from tutorial.items import SatackoverflowItem


class StackoverFlow(scrapy.Spider):
    name = "stackoverflow"
    page_number = 2

    def start_requests(self):
        urls = [
            # 'https://stackoverflow.com/users/'
            'https://stackoverflow.com/users?page=1&tab=reputation&filter=month'
            # 'https://stackoverflow.com/users?page=2&tab=reputation&filter=week'
            # 'https://stackoverflow.com/users/541136/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = SatackoverflowItem()
        all_quotes = response.css(".user-details")
        for quotes in all_quotes:
            name = quotes.css("a::text").extract()
            location = quotes.css(".user-location::text").extract()
            score = quotes.css(".reputation-score::text").extract()
            # tag = quotes.css(".user-tags::text").extract()
            # user_url = quotes.css(".user-details").xpath("@href").extract()

            items['name'] = name
            items['location'] = location
            items['score'] = score
            yield items

            # print("Total : ",counter)
        next_page = 'https://stackoverflow.com/users?page={}&tab=reputation&filter=month'.format((StackoverFlow.page_number))
        if StackoverFlow.page_number <= 100:
            StackoverFlow.page_number += 1
            print("******************* : ", StackoverFlow.page_number)
            yield response.follow(next_page, callback=self.parse)

        # next_page = response.css('div.s-pagination a::attr(href)').get()
        # print("+++++++++++++++++++++++++++++++++++ : ",next_page)
        # if next_page is not None:
        #     counter += 1
        #     print("******************* : ", next_page)
        #     print("Total : ", counter)
        #     yield response.follow(next_page, callback=self.parse)
