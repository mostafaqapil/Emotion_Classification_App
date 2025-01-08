# Emotion_Classification_App
# Emotion Classification Using Deep Learning

This project is an emotion classification application built using deep learning. The goal of the project is to classify emotions based on facial expressions using a Convolutional Neural Network (CNN). The application allows users to upload an image and predict the emotion of the person in the image.

## Project Overview

The Emotion Classification app uses a pre-trained deep learning model to predict the following emotions based on the uploaded face image:

- Angry
- Disgust
- Fear
- Happy
- Sad
- Surprise
- Neutral

The application is built using Python, TensorFlow/Keras, and Streamlit.

## Technologies Used

- **TensorFlow/Keras**: For building and running the deep learning model.
- **Streamlit**: For creating the interactive user interface.
- **NumPy**: For numerical operations and image processing.
- **PIL (Pillow)**: For image loading and resizing.

## Features

- Upload an image of a face.
- The model will predict the emotion (Angry, Disgust, Fear, Happy, Sad, Surprise, Neutral).
- The predicted emotion will be displayed on the interface.

## Installation

To run the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/emotion-classification.git
    ```

2. Navigate to the project directory:
    ```bash
    cd emotion-classification
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run Emotion_Classification_2.py
    ```

## Requirements

Make sure you have Python 3.6 or higher installed. The following libraries are required:

- **TensorFlow**: For building and using the CNN model.
- **Streamlit**: To run the app.
- **NumPy**: For numerical operations.
- **PIL**: For image processing.

To install the dependencies, use:

```bash
pip install tensorflow streamlit numpy pillow
