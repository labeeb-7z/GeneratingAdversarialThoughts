from fastapi import FastAPI, Request
import cv2 as cv
import urllib.request


import yunet
import mediapipee


app = FastAPI()


@app.post("/cv")
async def root(data: Request):
    req_info = await data.json()

    urllib.request.urlretrieve(req_info['url'], "sample.png")
    img = cv.imread("sample.png")
    # response = requests.get(req_info['url'])
    # img = Image.open(BytesIO(response.content))


    results = yunet.interface(img)
    results = [int (i) for i in results[0]]


    cv.rectangle(img, (results[0], results[1]), (results[0]+results[2], results[1]+results[3]), (0, 255, 0), 2)
    
    cv.imshow('Detected faces', img)
  
    cv.waitKey(0)
    cv.destroyAllWindows()


    return {"message": "Hello World"}

@app.post("/mp")
async def root(data: Request):
    req_info = await data.json()

    urllib.request.urlretrieve(req_info['url'], "sample.png")
    img = cv.imread("sample.png")
    # response = requests.get(req_info['url'])
    # img = Image.open(BytesIO(response.content))


    results = mediapipee.interface(img)