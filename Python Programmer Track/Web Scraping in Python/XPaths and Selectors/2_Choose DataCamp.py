'''
<html>
  <body>
    <div>
      <p>Hello World!</p>
      <div>
        <p>Choose DataCamp!</p>
      </div>
    </div>
    <div>
      <p>Thanks for Watching!</p>
    </div>
  </body>
</html>
'''
# Create an XPath string to the desired paragraph element
xpath = '/html/body/div/div/*'

# Print out the element text
print_element_text( xpath )
