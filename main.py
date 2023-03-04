from fastapi import FastAPI, Request
import cv2 as cv
import urllib.request


import yunet
import mediapipee
import haar
import age_gender


app = FastAPI()


@app.post("/cv")
async def root(data: Request):
    req_info = await data.json()

    urllib.request.urlretrieve(req_info['url'], "samkjple.png")
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


    return {"message": "faces found", "x1": results[0], "y1": results[1], "x2": results[2], "y2": results[3], "confidence": results[4]}
    



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



@app.post('/age')
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
