import cv2

from anime_face_detector import create_detector

detector = create_detector('yolov3')
image = cv2.imread('input.jpg')
preds = detector(image)
print(preds[0])