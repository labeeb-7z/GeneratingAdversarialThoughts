from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import cv2 as cv
import urllib.request
from urllib.request import Request as req
import base64

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'), ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'), ('Accept-Encoding','gzip, deflate, br'),\
    ('Accept-Language','en-US,en;q=0.5' ), ("Connection", "keep-alive"), ("Upgrade-Insecure-Requests",'1')]
urllib.request.install_opener(opener)

import yunet
import mediapipee
import haar
import age_gender
import detector
import catfish
from fastapi.middleware.cors import CORSMiddleware






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





@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/yunet")
async def root(data: Request):
    req_info = await data.json()

    # r = req(
    # url=req_info['url'],
    # headers={'User-Agent': 'Mozilla/5.0'}
    # )
    urllib.request.urlretrieve(req_info['url'], "sample.png")
    img = cv.imread("sample.png")

    if img is None : 
        return {"message": "Image not found"}

    # response = requests.get(req_info['url'])
    # img = Image.open(BytesIO(response.content))


    results = yunet.interface(img)
    
    if results is None:
        return {"message": "No faces found"}


    # cv.rectangle(img, (results[0], results[1]), (results[2], results[3]), (0, 255, 0), 2)  
    # cv.imshow('Detected faces', img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    with open('result.jpg', 'rb') as f:
        base64image = base64.b64encode(f.read())
    # return base64image
    # return FileResponse('result.jpg')

    return {"base64":base64image,"message": "faces found", "x1": results[0], "y1": results[1], "x2": results[2], "y2": results[3], "confidence": results[4]}
    



@app.post("/mp")
async def root(data: Request):
    req_info = await data.json()

    urllib.request.urlretrieve(req_info['url'], "sample.png")
    img = cv.imread("sample.png")
    if img is None : 
        return {"message": "Image not found"}


    results = mediapipee.interface(img)


    if results is None:
        return {"message": "No faces found"}
    
    print(results)
    return {"message": "faces found", "x1": results[0], "y1": results[1], "x2": results[2], "y2": results[3], "confidence": results[4]}


@app.post('/haar')
async def root(data: Request):

    req_info = await data.json()

    urllib.request.urlretrieve(req_info['url'], "sample.png")
    img = cv.imread("sample.png")

    if img is None :
        return {"message": "Image not found"}
    
    results = haar.interface(img)

    if results is None:
        return {"message": "No faces found"}

    return {"message": "faces found", "x1": results[0], "y1": results[1], "x2": results[2], "y2": results[3], "confidence": results[4]}



@app.post('/gender')
async def root(data: Request):
    req_info = await data.json()

    urllib.request.urlretrieve(req_info['url'], "sample.png")
    img = cv.imread("sample.png")

    if img is None :
        return {"message": "Image not found"}
    
    results = age_gender.interface(img)

    if results is None:
        return {"message": "No faces found"}

    return {"message": "faces found", "gender" : results[0], "age":results[1], "bounding boxes": results[2]}


@app.post('/fakedetector')
async def root(data: Request):
    req_info = await data.json()

    urllib.request.urlretrieve(req_info['url'], "sample.png")
    img = cv.imread("sample.png")

    if img is None :
        return {"message": "Image not found"}
    
    results = detector.detect()

    if results :
        return {"message": "Cartoon Image"}

    return {"message": "Non-Cartoon Image"}


@app.post('/catfish')
async def root(data: Request):
    req_info = await data.json()

    result = catfish.interface(req_info['url'])
    print(result)
    return result

    