import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

# Correct the import paths according to your environment setup
# If efficientnet is a custom module, ensure it's correctly installed or available in your project
from efficientnet.layers import Swish, DropConnect
from efficientnet.model import ConvKernelInitializer

# Register custom objects with TensorFlow
custom_objects = {
    'ConvKernelInitializer': ConvKernelInitializer,
    'Swish': Swish,
    'DropConnect': DropConnect,
}

# Adjust this path to where your model is actually stored
model_path = "/content/gdrive/MyDrive/Tooth_Shap_GPT/Deep_tooth/Model/Unflipped_Regress_Age(7-23)/Duo/26_Multi_1e-6_250_Unfreeze.h5"
model = load_model(model_path, custom_objects=custom_objects)


# Preparing and pre-processing the image
def preprocess_img(img_path):
    img = Image.open(img_path)
    img_resize = img.resize((224, 224))
    img2arr = img_to_array(img_resize)
    img_reshape = img2arr.reshape((1,) + img2arr.shape)
    return img_reshape


def predict_result(img_array):
    predictions = model.predict(img_array)
    prediction_age = predictions[0]
    prediction_gender = predictions[1]

    # Assuming your model returns age as a continuous value and gender as a probability that needs argmax
    # Adjust these lines according to your model's actual output format
    age = prediction_age[0][0]  # Assuming the first prediction is age as a continuous value
    gender = np.argmax(prediction_gender[0], axis=-1)  # Assuming the second prediction is gender as a binary classification

    return age, gender
