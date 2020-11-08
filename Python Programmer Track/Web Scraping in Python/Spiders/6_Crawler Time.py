# Import the scrapy library
import scrapy

# Create the Spider class
class DCdescr( scrapy.Spider ):
    name = 'dcdescr'
    # start_requests method
    def start_requests( self ):
        yield scrapy.Request( url = url_short, callback = self.parse )

    # First parse method
    def parse( self, response ):
        links = response.css( 'div.course-block > a::attr(href)' ).extract()
        # Follow each of the extracted links
        for link in links:
        yield response.follow( url = link, callback = self.parse_descr )

    # Second parsing method
    def parse_descr( self, response ):
        # Extract course description
        course_descr = response.css( 'p.course__description::text' ).extract_first()
        # For now, just yield the course description
        yield course_descr


# Inspect the spider
inspect_spider( DCdescr )
