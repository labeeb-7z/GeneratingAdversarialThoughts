import cv2
import mediapipe as mp
import time

mp_facedetector = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils




def interface(image) :
    with mp_facedetector.FaceDetection(min_detection_confidence=0.8) as face_detection:


    # Convert the BGR image to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process the image and find faces
        results = face_detection.process(image)
        # Convert the image color back so it can be displayed
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        x1 = None
        y1 = None
        x2 = None
        y2 = None

        confidence = None

        if results.detections:
            for id, detection in enumerate(results.detections):
                mp_draw.draw_detection(image, detection)

                bBox = detection.location_data.relative_bounding_box

                h, w, c = image.shape

                x1, y1, x2, y2 = int(bBox.xmin * w), int(bBox.ymin * h), int(bBox.width * w), int(bBox.height * h)
                
                confidence = detection.score[0]

                #cv2.putText(image, f'{int(detection.score[0]*100)}%', (boundBox[0], boundBox[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2)

        else :
            return None


        #cv2.putText(image, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 2)

        # cv2.imshow('Face Detection', image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        return x1, y1, x2, y2, confidence