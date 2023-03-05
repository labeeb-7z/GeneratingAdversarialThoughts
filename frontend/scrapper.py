import requests
from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
import json
import cv2
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from selenium.webdriver.firefox.options import Options
from fastapi.middleware.cors import CORSMiddleware


#creating function to scrap information
def TweetScrap(user):
    #url.format(urlObj) is the built in API provided by uRL class,which takes an object or string and return a formatted string
    #derived from that object or string and if urlObj not found then it throws an error.
    url = "https://twitter.com/{}/photo".format(user)

    # creating 'r' as an object that will hold the recieved data from http request.
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(url)

    bs = BeautifulSoup(driver.page_source)
    #holdin

    item = bs.find('img', alt="Image").attrs["src"]
    
    #returning parse(rep)
    return item

def InstaScrap(user):
    #url.format(urlObj) is the built in API provided by uRL class,which takes an object or string and return a formatted string
    #derived from that object or string and if urlObj not found then it throws an error.
    url = "https://www.instagram.com/{}".format(user)

    # creating 'r' as an object that will hold the recieved data from http request.
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(url)

    bs = BeautifulSoup(driver.page_source)
    #holding the title of bs

    #use of 'FIND' method to get the details.
    item = bs.find('meta',property ='og:image').attrs["content"]

    #returning parse(rep)
    return item

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def main():
    return {'message': 'Welcome to GeeksforGeeks!'}
    #TweetScrap(user)

class request_body(BaseModel):
    username : str

@app.post('/tweet')
def predict(data : request_body):
    
    image = TweetScrap(data.username)
    return {'img_url': image}

@app.post('/insta')
def predict(data : request_body):
    
    image = InstaScrap(data.username)
    return {'img_url': image}