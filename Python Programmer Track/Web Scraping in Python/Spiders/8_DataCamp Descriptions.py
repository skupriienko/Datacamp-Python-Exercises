# Import scrapy
import scrapy

# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess

# Create the Spider class
class DC_Description_Spider(scrapy.Spider):
  name = "dc_chapter_spider"
    # start_requests method
    def start_requests(self):
        yield scrapy.Request(url = url_short,
                            callback = self.parse_front)
    # First parsing method
    def parse_front(self, response):
        course_blocks = response.css('div.course-block')
        course_links = course_blocks.xpath('./a/@href')
        links_to_follow = course_links.extract()
        for url in links_to_follow:
        yield response.follow(url = url,
                                callback = self.parse_pages)
    # Second parsing method
    def parse_pages(self, response):
        # Create a SelectorList of the course titles text
        crs_title = response.xpath('//h1[contains(@class,"title")]/text()')
        # Extract the text and strip it clean
        crs_title_ext = crs_title.extract_first().strip()
        # Create a SelectorList of course descriptions text
        crs_descr = response.css( 'p.course__description ::text' )
        # Extract the text and strip it clean
        crs_descr_ext = crs_descr.extract_first().strip()
        # Fill in the dictionary
        dc_dict[crs_title_ext] = crs_descr_ext

# Initialize the dictionary **outside** of the Spider class
dc_dict = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(DC_Description_Spider)
process.start()

# Print a preview of courses
previewCourses(dc_dict)
