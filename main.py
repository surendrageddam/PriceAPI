from fastapi import FastAPI
from Scraper.scraper import Scraper


app = FastAPI()


@app.get("/")
async def home():
    return {"status": 200}


@app.get("/get")
async def get(url: str):
    url_scraper = Scraper(url)
    url_scraper.scrape()

    return{"price": url_scraper.price,"OutOfStock":url_scraper.OutOfStock}

