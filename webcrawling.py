import scrapy
import requests

# Display Reference Webpage
class WebReference(scrapy.Spider):
    name = "web_reference"
    start_urls = ['http://172.18.58.238/creative/']
    open("Output\\reference.json",'w').close()
    def parse(self, response):
       test = open("Output\\reference.json",'a')
       for link in response.css('a'):
           link_results = link.css('a::attr(href)').get()
           test.write(str({'web_reference': link_results})+"\n")
       test.close()