from fastapi import FastAPI
from Scraper.scraper import Scraper


app = FastAPI()


@app.get("/")
async def home():
    return {"status": 200}


@app.get("/get")
async def get_price(url: str):
    url_scraper = Scraper(url)
    url_scraper.scrape()

    return{"price": url_scraper.price}


@app.get("/check")
async def check_stock(url: str):
    url_scraper = Scraper(url)
    url_scraper.scrape()
    return {"OutOfStock": url_scraper.OutOfStock}
