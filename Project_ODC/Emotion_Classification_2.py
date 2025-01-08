
import streamlit as st 
from tensorflow.keras.models import load_model
import numpy as np 
from PIL import Image

model = load_model('./models/model_1.keras')



emotion_labels = ['Angry','Disgust','Fear','Happy','Sad','Surprise','Neutral']

st.title('Emotion Classification')
st.write('Upload an Image To Classify')

uploaded_file = st.file_uploader('Choose an Image',type=['jpg','jpeg','png'])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img,caption='Uploaded Image',use_column_width=True)
    img = img.convert('L')
    img = img.resize((48, 48), Image.Resampling.LANCZOS)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array,axis=-1)
    img_array = np.expand_dims(img_array,axis=0)
    
    prediction = model.predict(img_array)
    prediction_emotion = emotion_labels[np.argmax(prediction)]
    
    st.write(f'Predicted Emotion: {prediction_emotion}')
