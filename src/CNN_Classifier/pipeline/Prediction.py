import numpy as np
import os
from keras.models import load_model
from keras.utils import load_img, img_to_array

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load model
        model_path = os.path.join("artifacts", "training", "model.h5")
        model = load_model(model_path)

        # Load and preprocess image
        test_image = load_img(self.filename, target_size=(224, 224))
        test_image = img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)  # add batch dimension
        test_image = test_image / 255.0  # normalize pixel values

        # Make prediction
        result = np.argmax(model.predict(test_image), axis=1)
        preds = model.predict(test_image)
        print("Raw model output:", preds)
        print(result)

        if result[0] == 1:
            prediction = 'Normal'
        else:
            prediction = 'Adenocarcinoma Cancer'

        return [{"image": prediction}]
