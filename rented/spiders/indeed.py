# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy_splash import SplashRequest


class IndeedSpider(Spider):
    name = "indeed"
    # allowed_domains = ["www.indeed.com/jobs/search/?q=sofware-engineer&tm=14"]

    def start_requests(self):
        urls = ["https://www.indeed.com/jobs?q=software%20engineer&l=Irving%2C%20TX&vjk=fe9456a0b6ce20ce"]
        # urls = ['http://www.apartments.com/']
        for url in urls:

            yield SplashRequest(
                url,
                self.parse,
                args={
                    "wait": 3.5,
                },
            )

    def parse(self, response):
        
        titles = response.css('span::attr(title)').extract(),

        for title in titles:
            yield {
                'title': title,
            }

        page = response.url.split("/")[-2]
        filename = f"{page}.html"
        with open(filename, "wb") as f:
            f.write(response.body)
        self.log(f"Saved file {filename}")
        
