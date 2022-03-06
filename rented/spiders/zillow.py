import scrapy
from scrapy_splash import SplashRequest
import scrapy_splash


class ZillowSpider(scrapy.Spider):
    name = "zillow"

    def start_requests(self):
        urls = [
            "https://www.zillow.com/irving-tx/",
        ]
        for url in urls:
            # This is a Scrapy [SplashRequest](https://github.com/scrapy-plugins/scrapy-splash)
            yield SplashRequest(
                url,
                self.parse_result,
                args={
                    # optional; parameters passed to Splash HTTP API
                    "wait": 0.5,
                    # 'url' is prefilled from request url
                    # 'http_method' is set to 'POST' for POST requests
                    # 'body' is set to request body for POST requests
                },
                endpoint="render.json",  # optional; default is render.html
                splash_url="<url>",  # optional; overrides SPLASH_URL
                slot_policy=scrapy_splash.SlotPolicy.PER_DOMAIN,  # optional
            )
        
    def parse_result(self, response):
        
        # This is a Scrapy [Selector](https://doc.scrapy.org/en/latest/topics/selectors.html)
        

        
        for item in response.data['items']:
            yield {
                'address': item['address'],
                'price': item['price'],
                'url': item['url'],
                'bedrooms': item['bedrooms'],
                'bathrooms': item['bathrooms'],
                'square_feet': item['square_feet'],
                'lot_size': item['lot_size'],
                'year_built': item['year_built'],
                'type': item['type'],
                'image': item['image'],
                'description': item['description']
            }
        
        # Save the scraped data to a file
        with open('zillow.json', 'w') as f:
            f.write(response.body)

        
    
    