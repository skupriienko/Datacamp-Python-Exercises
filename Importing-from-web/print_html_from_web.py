# Import packages
# from urllib.request import urlopen, Request

# import bs4
# from bs4 import BeautifulSoup as soup
# from urllib.request import urlopen, Request
# response = urlopen('https://www.google.com')
# page_html = response.read()
# page_soup = soup(page_html, "html.parser")
# print(page_soup)

# # Specify the url
# url = "http%3A//www.datacamp.com/teach/documentation"

# # This packages the request
# request = Request(url)

# # Sends the request and catches the response: response
# response = urlopen(request)

# # Extract the response: html
# html = response.read()

# # Print the html
# print(html)

# # Be polite and close the response!
# response.close()

import urllib
urllib.urlopen('https://google.com').read()
