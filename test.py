import httpx 
from selectolax.parser import HTMLParser
from bs4 import BeautifulSoup
import uvicorn
import requests
class ScrapTest:
   def __init__(self):
     self.name = "Hello"
     self.url = "https://realpython.github.io/fake-jobs/"
     self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
     self.content = []
     
     
   def run_server(self): 
    
    data = self.test_scraping()
     
    
     
   def test_scraping(self):
    content = [] 
    resp = httpx.get(self.url, headers=self.headers)   
    soup = BeautifulSoup(resp.content, "html.parser")
    resultsContainer = soup.find(id="ResultsContainer")
    
    job_elements = resultsContainer.find_all("div", class_="card-content")
    
    for jobs in job_elements:
      title = jobs.find("h2", class_="title")
      company = jobs.find("h3", class_="company")
      location = jobs.find("p", class_="location")
      apply_now = jobs.find("a", class_="card-footer-item", string="Apply")
      
      
      content.append(
        {
          "title": title.text.strip(),
          "company": company.text.strip(),
          "location": location.text.strip(),
          "apply_link": apply_now["href"],
        
          
        }
      )
     
    return content  
    

class Pokemon:
  def __init__(self):
    self.url = "https://scrapeme.live/shop/"
    self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
  
  def scrap_pokemons(self):
    content = []
    resp = httpx.get(self.url, headers=self.headers)
    soup = BeautifulSoup(resp.content, "html.parser")
    
    products = soup.find_all("li", class_="product")
    
    for product in products:
      image = product.find('img', class_="attachment-woocommerce_thumbnail size-woocommerce_thumbnail wp-post-image")
      image_src = image['src']
      
      title = product.find('h2', class_="woocommerce-loop-product__title").text.strip()
      price = product.find('span', class_="woocommerce-Price-amount amount").text.strip()
      
      content.append(
        {
          "image_url": image_src,
          "title": title,
          "price": price
        })
    
    return(content)
    

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
    
    print(content)

  def latest_movie_detail(self, title: str) -> list:
    content = []
    url = "https://fzmovies.net/movie-The Red 2024--hmp4.htm"
    resp = httpx.get(url=url, headers=self.headers)
    soup = BeautifulSoup(resp.content, "html.parser")
    
    title = soup.find("div", class_="moviename").find("span").text
    image_url = soup.find("div", class_="moviedesc").find("span").find("img")["src"]
    description = soup.find("div", class_="moviedesc").find_all("textcolor1")
    actor = soup.find("div", class_="moviedesc").find("div", itemprop="actor").find_all("meta")
    actors = []
    for act in actor:
      actors.append(act['content'])
      
    director = soup.find("div", class_="moviedesc").find("div", itemprop="director").find_all("meta")
    directors = []
    for act in director:
      directors.append(act['content'])  
    
    
    genre = soup.find("div", class_="moviedesc").find_all("span", itemprop="genre")
    genres = []
    for act in genre:
      genres.append(act.text)
    
    print(title)
    print(f"https://fzmovies.net{image_url}")
    print(description[0].text)
    print(description[1].text)
    print(actors)
    print(directors)
    
    print(genres)
    

pok = Pokemon()
pok.scrap_pokemons()
