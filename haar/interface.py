import cv2
import numpy as np

def interface(img):

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    haar_cascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')

    detection_result, rejectLevels, levelWeights =haar_cascade.detectMultiScale3(gray_img, scaleFactor=1.0485258, minNeighbors=6, minSize=(30,30), outputRejectLevels = 1)

    if len(detection_result) == 0:
        return None
    
    idx=0
    #finding only one image
    if len(detection_result) > 1 :
        idx = np.argmax(levelWeights)
        detection_result = detection_result[idx]
    else :
        detection_result = detection_result[0]

    detection_result = detection_result.tolist()

    return detection_result[0],detection_result[1],detection_result[2],detection_result[3] , levelWeights[idx]

    #finding all images
    # for (x, y, w, h) in detection_result:

    #     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    #     cv2.imshow('Detected faces', img)
        
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()