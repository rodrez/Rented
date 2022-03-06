import scrapy
from scrapy_splash import SplashRequest

from .utils import export_html


class ApartmentsSpider(scrapy.Spider):
    name = "apartments"
    allowed_domains = ["www.apartments.com"]
    # start_urls = ['http://www.apartments.com/']

    def start_requests(self):
        urls = [
            "https://www.apartments.com/houses/plano-tx/",
            "https://www.apartments.com/houses/plano-tx/2/",
            "https://www.apartments.com/houses/irving-tx/",
            "https://www.apartments.com/houses/irving-tx/2/",
            "https://www.apartments.com/houses/arlington-tx/",
            "https://www.apartments.com/houses/arlington-tx/2/",
            "https://www.apartments.com/houses/arlington-tx/3/",
            "https://www.apartments.com/houses/arlington-tx/4/",
            "https://www.apartments.com/houses/arlington-tx/5/",
            "https://www.apartments.com/houses/arlington-tx/6/",
            "https://www.apartments.com/houses/arlington-tx/7/",
            "https://www.apartments.com/houses/coppell-tx/",
        ]
        for url in urls:

            yield SplashRequest(
                url,
                self.parse,
                args={
                    "wait": 0.5,
                },
            )

    def parse(self, response):
        # prices from class "property-pricing" of a p tag
        prices = response.css("div.price-range::text").extract()

        # address from class "property-address" of a div tag
        addresses = response.css("div.property-address::text").extract()

        # Bed range from class "bed-range" of a div tag
        bed_ranges = response.css("div.bed-range::text").extract()

        # title from class "js-placardTitle title" of a span tag
        titles = response.css("span.js-placardTitle::text").extract()

        # Links from class "property-link" of a tag
        links = response.css("a.property-link::attr(href)").extract()

        # for title, price, address, bed_range, link in zip(titles, prices, addresses, bed_ranges, links):
        #     yield {
        #         'title': title,
        #         'price': price,
        #         'address': address,
        #         'bed_range': bed_range,
        #         'link': link,
        #     }

        for prop in response.css("div.property-info"):

            yield {
                "title": prop.css("div > div > a > div::text").extract_first().strip(),
                "address": prop.css("div > div > a > div.property-address::text").extract_first().strip(),
                "price": prop.css("div > a.property-link > div > div div > div.price-range::text").extract_first().strip(),
                "beds": prop.css("div > a.property-link > div > div div > div.bed-range::text").extract_first().strip(),
                "link": prop.css("div > a.property-link::attr(href)").extract_first(),                
            }

        # export_html(response)
