import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

new_model = tf.keras.models.load_model('detector/my_model')

def load_image(img_path, show=False):

    img = image.load_img(img_path, target_size=(224, 224))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

    return img_tensor

# img = load_image('human.jpeg') # Your image path
# prediction = new_model.predict(img)

# print(prediction)


def detect() :
    img = load_image('sample.png')
    prediction = new_model.predict(img)[0]

    if prediction[0]>0.5 : 
        return True
    else :
        return False