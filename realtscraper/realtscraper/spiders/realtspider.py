import scrapy

class RealtSpider(scrapy.Spider):
    name = 'realt'
    start_urls = ['https://www.moyareklama.by/%D0%93%D0%BE%D0%BC%D0%B5%D0%BB%D1%8C/%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80%D1%8B_%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0/']

    def parse(self, response):
        for appartms in response.css('div.one_advert_list'):
            yield {
                'title': appartms.css('a.premium::text').get(),
                'address': appartms.css('div.address::text').get(),
                'price': appartms.css('div.price::text').get().replace(' р.',''),
                'link': appartms.css('a.premium').attrib['href'],
            }

