# Create a CSS Locator string to the desired hyperlink elements
css_locator = 'a.course-block__link'

# Select the hyperlink elements from response and sel
response_as = response.css(css_locator)
sel_as = sel.css(css_locator)

# Examine similarity
nr = len( response_as )
ns = len( sel_as )
for i in range( min(nr, ns, 2) ):
    print( "Element %d from response: %s" % (i+1, response_as[i]) )
    print( "Element %d from sel: %s" % (i+1, sel_as[i]) )
    print( "" )
