import json
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


class Scraper:

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
    re_session = requests.session()

    def __init__(self, url):
        self.url = url

    def scrape(self):
        page = Scraper.re_session.get(self.url, headers=Scraper.headers)
        soup = BeautifulSoup(page.content, "html.parser")
        if 'www.myntra.com' in self.url:
            self.price = int(json.loads(soup.find_all('script')[1].string)[
                'offers']['price'])
            self.OutOfStock = json.loads(soup.find_all('script')[1].string)[
                'offers']['availability'] != "InStock"
        elif 'www.ajio.com' in self.url:
            self.price = int(json.loads(soup.find_all('script')[6].string)[
                'offers']['price'])
            self.OutOfStock = json.loads(soup.find_all('script')[6].string)[
                'offers']['availability'] != "https://schema.org/InStock" or "https://schema.org/LimitedAvailability"
        else:
            raise Exception('URL is invalid')
