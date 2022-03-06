from tracemalloc import start
import scrapy
from scrapy_splash import SplashRequest


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]

    def start_requests(self):
        urls = ["http://quotes.toscrape.com/"]
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

        for quote in response.css('div.col-md-8'):
            yield {
                'author': quote.css('small.author::text').get(),
                'quote': quote.css('span.text::text').get(),
            }
        
        
        # page = response.url.split("/")[-2]
        # filename = f"quotes-{page}.html"
        # with open(filename, "wb") as f:
        #     f.write(response.body)
        # self.log(f"Saved file {filename}")
        # Save the scraped data to a file
        # with open('zillow.json', 'w') as f:
        #     f.write(response.body)
