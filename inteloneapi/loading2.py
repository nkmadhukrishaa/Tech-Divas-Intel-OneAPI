from PIL import Image
import tensorflow as tf
from tensorflow import keras 
from tensorflow.keras import models,layers

import numpy as np

class_names = ['BellPepper_BacterialSpot',
 'BellPepper_Healthy',
 'Maize_CercosporaLeafSpot',
 'Maize_CommonRust ',
 'Maize_Healthy',
 'Maize_NorthernLeafBlight',
 'Potato_EarlyBlight',
 'Potato_Healthy',
 'Potato_LateBlight',
 'Rice_BrownSpot',
 'Rice_Healthy',
 'Rice_Hispa',
 'Rice_LeafBlast',
 'Tomato_BacterialSpot',
 'Tomato_EarlyBlight',
 'Tomato_Healthy',
 'Tomato_LateBlight',
 'Tomato_SeptoriaLeafSpot',
 'Tomato_YellowLeafCurlVirus']

#k=image_path_to_np_array("D:\Visual studio\Chin python\.vscode\oneapi wkshp\inteloneapi\CropDisease\Maize_CercosporaLeafSpot\maize1.jpg")
#print(k)
def loading(image_path):
    def image_path_to_np_array(image_path):
        try:
            # Read the image using PIL
            image = Image.open(image_path)

            # Convert the image to a NumPy array
            image_array = np.array(image)

            # If the image has an alpha channel, remove it
            if image_array.shape[-1] == 4:
                image_array = image_array[:, :, :3]
            return image_array

        except Exception as e:
            print(f"Error: {e}")
            return None
    
    model_path = 'D:\Visual studio\Chin python\.vscode\oneapi wkshp\inteloneapi\CD3.h5'
    loaded_model = tf.keras.models.load_model(model_path)
    img_array=tf.keras.preprocessing.image.img_to_array(image_path_to_np_array(image_path))
    img_array=tf.expand_dims(img_array,0)
    

    # Make a prediction using the loaded model
    predictions = loaded_model.predict(img_array)
    predicted_class=class_names[np.argmax(predictions[0])]
    confidence=round(100*(np.max(predictions[0])),2)
    return predicted_class,confidence

#l=loading("D:\Visual studio\Chin python\.vscode\oneapi wkshp\inteloneapi\CropDisease\Maize_CercosporaLeafSpot\maize1.jpg")


