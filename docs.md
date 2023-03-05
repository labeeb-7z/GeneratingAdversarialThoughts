## Fake Profile Detection API - Documentaion

---

A feature rich API dedicated towards using Computer Vision techniques on input profile picture and identify potentially fake profiles.

We've focused on the following primary features : 

- Provide different inference models to the users, so they can use the one with a balance of latency and accuracy as per their task.
- Identify false Positives :  Detect cartoon/anime faces in the input images and distinguish them from human faces.
- Provide Additional details about the input image including Age, Gender, Potential Celebrity match, if its AI Generated, etc which might be relevant in fake profile detection.

---

## API Reference


[/yunet](#yunet)

[/mp](#mediapipe)

[/haar](#haarcascade)

[/gender](#gender-and-age)


[/fakedetector](#false-positive-detector)


---


### Yunet
`POST https://example.com/yunet`

**Description** : This endpoint uses Yunet model from opencv_zoo to detect human faces in the input image. It returns the coordinates of the bounding boxes around the face and a confidence socre.
Confidence score is a number between 0-1 indicating the confidence of  model in its prediction.
If multiple faces are detected, it returns the one with maximum confidence score.

**Request Body** : 
```jsonld
{
    "url" : "input/image/url"
}
```
**Response Body** : 

if image is not found on input url : `"message": "Image not found"}`

if no face is detected in input image : ```{"message": "No faces found"}```

faces found : 
```jsonld
{
"message": "faces found",
"x1": _ #top left x co-ordinate ,
"y1": _ #top left y co-ordinate,
"x2": _ #bottom right x co-cordinate,
"y2": _ #bottom right y co-cordinate,
"confidence": _ #
}
```

---

### Mediapipe

`POST https://example.com/mp`

**Description** : This endpoint uses Mediapipe's Face detection model to detect human faces in the input image. It returns the coordinates of the bounding boxes around the face and a confidence socre.
Confidence score is a number between 0-1 indicating the confidence of  model in its prediction.
If multiple faces are detected, it returns the one with maximum confidence score.

**Request Body** : 
```jsonld
{
    "url" : "input/image/url"
}
```

**Response Body** : 

if image is not found on input url : ``{"message": "Image not found"}``

if no face is detected in input image : ``{"message": "No faces found"}`

faces found : 
```jsonld
{
"message": "faces found",
"x1": _ #top left x co-ordinate ,
"y1": _ #top left y co-ordinate,
"x2": _ #bottom right x co-cordinate,
"y2": _ #bottom right y co-cordinate,
"confidence": _ #
}
```
---

### Haarcascade

`POST https://example.com/haar`

**Description** : This endpoint uses Haarcascade developed by opencv to detect human faces in the input image. It returns the coordinates of the bounding boxes around the face and a confidence socre.
Confidence score is a number between 0-1 indicating the confidence of  model in its prediction.
If multiple faces are detected, it returns the one with maximum confidence score.

**Request Body** : 
```jsonld
{
    "url" : "input/image/url"
}
```
**Response Body** : 

if image is not found on input url : `{"message": "Image not found"}`

if no face is detected in input image : ``{"message": "No faces found"}`

faces found : 
```jsonld
{
"message": "faces found",
"x1": _ #top left x co-ordinate ,
"y1": _ #top left y co-ordinate,
"x2": _ #bottom right x co-cordinate,
"y2": _ #bottom right y co-cordinate,
"confidence": _ #
}
```
---

### Gender and Age

`POST https://example.com/gender`

**Description** : This endpoint uses a trained model each for predicting the age and gender. It initially crops out the face part detected by other models and passes it to both the models.

It predicts either Male of Female for the Gender.
The Age prediction is divided into the following the classes : 
``['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']``

The age prediction will denote one these ranges.



**Request Body** : 
```jsonld
{
    "url" : "input/image/url"
}
```
**Response Body** : 

if image is not found on input url : `{"message": "Image not found"}`

if no face is detected in input image : `{"message": "No faces found"}`

faces found : 
```jsonld
{
"message" : "faces found",
"gender" : _ #male or female,
"age" : _ #age range
"bounding boxes " : _ #bounding boxes of detected face
}
```
---

### False Positive 

`POST https://example.com/fakedetector`

**Description** : This endpoint is used to detect cartoon/anime faces which look similar to human faces but are actually not.

The underlying model used is built on top of VGG-16, using transfer learning to distinguish human faces and cartoons.



**Request Body** : 
```jsonld
{
    "url" : "input/image/url"
}
```

**Response Body** : 

if image is not found on input url : ``{"message": "Image not found"}`


if cartoon is detected : 
``{"message": "Cartoon Image"}``

if cartoon is not detected : 
`{"message": "Non-Cartoon Image"}`