from scrapy import Selector, Response

# Create a selector object from a secret website
# sel = Selector( text = html )

# url = 'https://kuprienko.info'
# Get the URL to the website loaded in response
this_url = response.url

# Get the title of the website loaded in response
this_title = response.xpath( '/html/head/title/text()' ).extract_first()

# Print out our findings
print_url_title( this_url, this_title )
