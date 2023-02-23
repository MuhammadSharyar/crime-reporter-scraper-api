from fastapi import FastAPI
from scraper import Scraper

app = FastAPI()
reports = Scraper()


@app.get("/")
async def read_items():
    return reports.scrapedata()