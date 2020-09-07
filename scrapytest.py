import scrapy
import requests

def recon():

# Set the target webpage
    url = 'http://www.wikipedia.org/'
    r = requests.get(url)

# Display Output Get and Ok
    print("Status code:")
    print("\t *", r.status_code)

# Display Website Header
    h = requests.headers(url)
    for x in h.headers:
        print("\t", x, '.', h.headers[x])

# Modify the headers user-agent
    headers = {
        'User-Agent': 'Mobile'
    }
    url2 = 'http://httpbin.org/headers'
    rh = requests.get(url2, headers=headers)
    print(rh.text)


    recon = open("output\\recon.txt", "w")
    recon.write(f"{r.status_code}\n{requests.headers(url,url2)}\n$$$ Modded: \n{headers}\n{request.headers(url,url2)}")

# Display Reference Webpage
class WebReference(scrapy.Spider):
    name = "web_reference"
    start_urls = ['http://www.wikipedia.org/']

    def parse(self, response):
        xpath_selector = '//link'
        for x in response.css(xpath_selector):
            newsel = '@src'
            yield {
                'reference webpage': x.xpath(newsel).extract_link,
            }
        # To recurse next page
        page_selector = '.next a ::attr(href)'
        next_page = response.css(page_selector).extract_link
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

# Extract Image Links (.JPG)
class ImageLink(scrapy.Spider):
    name = "image_link"
    start_urls = ['http://www.wikipedia.org/']

    def parse(self, response):
        xpath_selector = '//img'
        for i in response.css(xpath_selector):
            newsel = '@src'
            yield {
                'Image Link': i.xpath(newsel).extract_first(),
            }

# To recurse next page
        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
