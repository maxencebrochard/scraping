import scrapy
import re

class AcparisSpier(scrapy.Spider):
    name = "acparis"

    start_urls = [
    "https://www.ac-paris.fr/portail/recherche?action=upListe&dis=B&titre=EST",
    "https://www.ac-paris.fr/portail/recherche?action=upListe&dis=D&titre=SUD",
    "https://www.ac-paris.fr/portail/recherche?action=upListe&dis=E&titre=OUEST",
    "https://www.ac-paris.fr/portail/recherche?action=upListe&dis=A&titre=NORD"
    ] 

    def parse(self, response):
        
        print(response.url)

        print("\n")


        onclick_list = response.xpath("//li/a/@onclick").extract()
        
        for onclick in onclick_list:
            search_object = re.search(r"(?<=&id=).*(?=')", onclick)
            id = search_object.group()
            url = u'https://www.ac-paris.fr/portail/recherche?action=upDetail&id=' + id
            
            yield scrapy.Request(url=url, callback=self.parseSchool)


        
    def parseSchool(self,response):
        '''

        //h1/text()

        //a/@href

        //a/@onclick

        ''' 

        school = {}


        title = response.xpath(" //h1/text()").extract_first()

        mail = None
        hrefs = response.xpath('//a/@href').extract()

        for href in hrefs:
            search_object = re.search(r"(?<=mailto:).*",href)
            if not(search_object == None):
                mail = search_object.group()


        address = None
        onclicks = response.xpath('//a/@onclick').extract()

        for onclick in onclicks:
            search_object = re.search(r"(?<=javascript:load\(').*(?=')",onclick)
            if not(search_object == None):
                address = search_object.group()

        print(type(title))
        print(title)
        
        title = title.encode('utf-8', 'ignore')
        mail = mail.encode('utf-8', 'ignore')
        address = address.encode('utf-8', 'ignore')

        #print(mail)
        #print(address)

        school["title"] = title
        school["mail"] = mail
        school["address"] = address

        yield school

        #print("---------")
