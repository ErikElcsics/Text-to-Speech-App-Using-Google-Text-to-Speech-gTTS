# Instant Text-to-Speech App - Using Google Text-to-Speech (gTTS)

## Summary

This is a simple **Text-to-Speech (TTS)** app built using **Streamlit** and **Google Text-to-Speech (gTTS)**. It allows users to type in any text, adjust the speech rate, and then convert the text to speech instantly. The app uses the **gTTS** library, which provides easy integration of Google's TTS engine to convert text to speech in multiple languages.

## Features

- **Text-to-Speech Conversion**: Converts any entered text to speech using Google’s TTS engine.
- **Speech Rate Control**: Allows users to control the rate (speed) of speech using a slider.
- **Instant Playback**: Instantly plays the converted audio once the text is entered and the "Convert to Speech" button is clicked.
- **Simple User Interface**: Easy-to-use interface built with Streamlit.
- **Audio Download**: Provides an option to download the generated speech as an MP3 file.

## About Google Text-to-Speech (gTTS)

Google Text-to-Speech (gTTS) is a Python library that interfaces with Google Translate’s TTS API. It converts text into speech and supports multiple languages. The library allows you to generate speech using different languages and customize the speed of the speech. The generated audio can then be saved and played back easily.

## Installation Instructions

To run the app locally, follow these steps:

1. **Clone the Repository**:
    
    git clone https://github.com/ErikElcsics/Text-to-Speech-App-Using-Google-Text-to-Speech-gTTS.git
    cd Instant-Text-to-Speech-App
    

2. **Install Required Libraries**:
    You can install the required libraries using the following pip commands:

    
    pip install streamlit gtts
    

3. **Run the Streamlit App**:
    Start the Streamlit app by running the following command:

    
    streamlit run TextToSpeechApp.py
    

4. Open your browser and go to `http://localhost:8501` to interact with the app.

## How the Code Works

The app provides an interface where users can input text, adjust the speech rate, and trigger the TTS conversion. Here's a summary of the process:

1. **Streamlit UI**: The app uses Streamlit for a simple and interactive user interface. The UI consists of a text area for the user to input text, a slider to adjust the speech rate, and a button to trigger the TTS conversion.
2. **Text-to-Speech Conversion**: When the user clicks the "Convert to Speech" button, the app uses the `gTTS` library to convert the entered text into speech. The text is passed to the `gTTS` function, which generates the audio file in MP3 format.
3. **Playback**: The generated MP3 file is saved to the disk and played back using Streamlit’s `st.audio()` function. The audio is played instantly after conversion.
4. **Adjustable Speech Rate**: The user can adjust the speed of the speech using the slider. The value selected on the slider is passed to the `gTTS` function to adjust the speed of the generated speech.

## How to Use the App

1. **Type Your Text**: Enter any text you want to be converted to speech in the text input box.
2. **Adjust Speech Rate**: Use the slider to adjust the speech rate (speed). The default is 150, but you can choose a value between 50 and 200.
3. **Convert to Speech**: Click the "Convert to Speech" button, and the app will generate speech for your text. The audio will be played back instantly.
4. **Listen & Enjoy**: Listen to your text being spoken out loud! You can also download the MP3 file for later use.

## Libraries Used

- **Streamlit**: A Python framework for building interactive web apps. Used for building the UI of the app.
- **gTTS (Google Text-to-Speech)**: A Python library to convert text to speech using Google's Text-to-Speech API.
- **os**: Used to handle file operations for saving the generated speech.

## Summary of How the App Works

### From a User’s Perspective:
- The user simply types text into the input box and clicks the button to convert the text to speech.
- The app instantly converts the text to speech, plays the audio, and allows the user to listen to the generated speech.
- The user can control the speech rate using a slider.

### From a Technical Perspective:
- The app uses **Streamlit** for the front-end interface, where users can input text and interact with the app.
- The **gTTS** library is used to convert the user-provided text into speech, saving the result as an MP3 file.
- The generated audio is played using **Streamlit’s** `st.audio()` function, and the speech rate is adjustable through a slider input.

![image](https://github.com/user-attachments/assets/bcbcbc82-89a1-47ea-b972-59d798dd99ee)
