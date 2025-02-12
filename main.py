from typing import Union
import httpx 
from selectolax.parser import HTMLParser
import requests
from bs4 import BeautifulSoup
import uvicorn
from fastapi import FastAPI

class Movie:
  def __init__(self):
    self.url = "https://fzmovies.net/movieslist.php?catID=2&by=date"
    self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
  
  def scrap_latest_movies(self):
    content = []
    resp = httpx.get(self.url, headers=self.headers)
    soup = BeautifulSoup(resp.content, "html.parser")
   
    
    movie_card = soup.find_all("div", class_="mainbox")
    
    for movie in movie_card:
      image = movie.find("img")
      finde = movie.find("a")
      title = movie.find("b")
      
      content.append(
        {
          "id": len(content) + 1,
          "title": title.text,
          "movie_url": finde['href'],
          "image_url": image['src']
        }
      )
    
    return content


movies = Movie()
latest = movies.scrap_latest_movies()


app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "Hello there!"}

@app.get("/latest")
async def read_jobs():
    return {"data": latest}



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
