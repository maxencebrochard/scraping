import scrapy
import requests

#class QuotesSpider(scrapy.Spider):
#    name = "quotes"
#
#    def start_requests(self):
#        urls = [
#            'http://quotes.toscrape.com/page/1/',
#            'http://quotes.toscrape.com/page/2/',
#        ]
#        for url in urls:
#            yield scrapy.Request(url=url, callback=self.parse)
#
#    def parse(self, response):
#        page = response.url.split("/")[-2]
#        filename = 'quotes-%s.html' % page
#        with open(filename, 'wb') as f:
#            f.write(response.body)
#        self.log('Saved file %s' % filename)
#        


gcPreResp = requests.get("https://connect.garmin.com/fr-FR/signin", allow_redirects=True)
text = gcPreResp.text
username = "ceciestuntest14@gmail.com"
password = "Ceciestuntest1"

params = {"login": "login", "login:loginUsernameField": username, "login:password": password, "login:signInButton": "Sign In"}

resp = requests.post("https://connect.garmin.com/signin", data=params, allow_redirects=False, cookies=gcPreResp.cookies)

text = requests.get("https://connect.garmin.com/modern/groups ", allow_redirects=False)
