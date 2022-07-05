from scrapy import Request
import scrapy
import re

class BukuSpider(scrapy.Spider):
    name = 'buku'
    allowed_domains = ['bukukita.com']
    main_url = 'https://www.bukukita.com/katalogbuku.php?page='
    start_urls = [main_url+str(999)]

    def parse(self, response):
        max_page = response.css('ul.pagination a::text').getall()[-1]
        for i in range(1,int(max_page)+1):
            yield Request(self.main_url+str(i),callback=self.next_parse)

    def next_parse(self, response):
        '''Parse the start urls and look for books url'''

        # find all books urls
        catalog = response.css('div.product-grid a::attr(href)')
        for url in catalog:
            url = response.urljoin(url.get())
            yield Request(url,callback=self.find_details)

    def find_details(self, response):
        '''Look for book details information'''

        # find details
        rows = response.css('div.row')
        book = {"source": response.url}
        for row in rows:
            cols = row.css('div[class*=col]')
            if len(cols) == 2:
                key = cols[0].css('::text').get()
                key = re.sub("\s+"," ",key).strip()
                value = cols[1].css('::text').get()
                value = re.sub("\s+"," ",value).strip()
                if key == "Text Bahasa":
                    value = " ".join(re.findall("\w+",value))
                if key != "":
                    book.update({key:value})
        yield book