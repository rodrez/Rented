import scrapy
from scrapy_splash import SplashRequest

class TruliaSpider(scrapy.Spider):
    name = "trulia"
    allowed_domains = ["www.trulia.com"]

    def start_requests(self):
        urls = ["http://www.trulia.com/"]

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
        for rental in response.xpath('//*[@id="resultsColumn"]/div[1]/ul'):
            yield {
                # Find price based on attribute data-testid
                "price": rental.xpath('//*[@id="resultsColumn"]/div[1]/ul/li[1]/div/div/div/div/div[1]/div[2]/div/div[1]/div[1]/div/text()').extract(),
            }
