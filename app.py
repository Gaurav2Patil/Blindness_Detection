import cv2
import numpy as np
import streamlit as st
from keras.models import load_model

# Load the saved model
model = load_model('blindness.model')

st.title("Blindness Prediction App")
st.write("Upload an image and click 'Predict' to determine the predicted class index.")

uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    # Read and preprocess the uploaded image
    image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), 1)
    image = cv2.resize(image, (100, 100))
    image = np.expand_dims(image, axis=0)

    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Make prediction when the 'Predict' button is clicked
    if st.button("Predict"):
        prediction = model.predict(image)
        predicted_class_index = np.argmax(prediction)

        # Print the prediction
        st.write(f"Predicted class index: {predicted_class_index}")
