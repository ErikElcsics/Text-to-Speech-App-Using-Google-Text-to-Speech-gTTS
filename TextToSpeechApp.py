import streamlit as st
from gtts import gTTS
import os

# Streamlit UI
st.title("Instant Text to Speech App - Using Google Text-to-Speech (gTTS)")

# Input text box
text_input = st.text_area("Simply type your text here, and let the magic happen as we turn your text into voice in an instant:", "Hey there! I'm Erik Elcsics, your friendly AI developer, and welcome to the Text-to-Speech app! Ever wondered how your words would sound if they could speak for themselves? Well, wonder no more! Simply type anything here, hit play, and let the magic happen as we turn your text into voice in an instant! Ready to hear your thoughts come to life? Let's go!")

# Adjusting speech rate
rate = st.slider("Rate of speech (Speed)", 50, 200, 150)

# Button to trigger TTS
if st.button("🎤 Convert to Speech"):
    # Using gTTS to convert text to speech
    tts = gTTS(text_input, lang='en', slow=False)  # slow=False for normal speed
    tts.save("output.mp3")

    # Play the saved audio file
    st.audio("output.mp3", format="audio/mp3")
    st.success("🎙️ Speaking the text!")

