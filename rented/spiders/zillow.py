import scrapy
from scrapy_splash import SplashRequest
import scrapy_splash


class ZillowSpider(scrapy.Spider):
    name = "zillow"
    allowed_domains = ["zillow.com"]

    def start_requests(self):
        urls = [
            
            # "https://docs.scrapy.org/en/1.2/intro/tutorial.html",
            "https://www.zillow.com/homes/for_rent/",
        ]
        for url in urls:
            # This is a Scrapy [SplashRequest](https://github.com/scrapy-plugins/scrapy-splash)
            yield SplashRequest(
                url,
                self.parse,
                args={
                    # optional; parameters passed to Splash HTTP API
                    "wait": 0.5,
                    # 'url' is prefilled from request url
                    # 'http_method' is set to 'POST' for POST requests
                    # 'body' is set to request body for POST requests

                },
            )
        

    def parse(self, response):
        for rental in response.xpath('//*[@id="grid-search-results"]/ul'):
            yield {
                'price': rental.css("div.list-card-price::text").extract(),
                'details': rental.css('div.list-card-details::text').extract(),
                'address': rental.css('div.list-card-addr::text').extract(),
            }
        
       

    
    