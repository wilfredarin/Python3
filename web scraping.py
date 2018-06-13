import requests
from lxml import html
 
# url to scrape data from
link = 'https://timesofindia.indiatimes.com/'
 
# path to particular element
path = '/html/body'
 
response = requests.get(link)
byte_string = response.content
 
# get filtered source code
source_code = html.fromstring(byte_string)
 
# jump to preferred html element
tree = source_code.xpath(path)
 
# print texts in first element in list
print(tree[0].text_content())