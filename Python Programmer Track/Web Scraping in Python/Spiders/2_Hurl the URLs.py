# help(inspect_class)
# Help on function inspect_class in module __main__:

# inspect_class(c)

# Import scrapy library
import scrapy

# Create the spider class
class YourSpider( scrapy.Spider ):
    name = "your_spider"
    # start_requests method
    def start_requests( self ):
        urls = ["https://www.datacamp.com", "https://scrapy.org"]
        for url in urls:
        yield url
    # parse method
    def parse( self, response ):
        pass

# Inspect Your Class
inspect_class( YourSpider )
