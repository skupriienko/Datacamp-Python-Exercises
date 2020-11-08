from scrapy import Selector

# Create a selector from the html (of a secret website)
sel = Selector( text = html )

# Fill in the blank
css_locator = ( 'div.course-block > a' )

# Print the number of selected elements.
how_many_elements( css_locator )
