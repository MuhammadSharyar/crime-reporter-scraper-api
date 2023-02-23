from fastapi import FastAPI
from scraper import Scraper
import uvicorn

app = FastAPI()
reports = Scraper()


@app.get("/")
async def read_items():
    return reports.scrapedata()


if __name__ == '__main__':
    uvicorn.run(app)