import requests
import streamlit as st
import base64
import io
import os
from dotenv import load_dotenv

def generating_audio(text):
    """
    Generates audio from text using the Sarvam AI Text-to-Speech API.

    Args:
    text (str): The input text that will be inferences into an audio.

    Returns:
    BytesIO: An in-memory file-like object containing the audio data in WAV format.
    """

    # Loading environment variables from the .env file
    load_dotenv()

    # API endpoint for Sarvam AI Text-to-Speech service
    url = "https://api.sarvam.ai/text-to-speech"

    # Preparing the payload with the necessary parameters for the API request
    payload = {
        "inputs": [text],  # text inputs to convert to speech
        "target_language_code": "hi-IN",  # Target language code (Hindi - India)
        "speaker": "meera",  # Specify the speaker's voice (Meera)
        "pitch": 0,  # Pitch of the voice (0 is default)
        "pace": 1.00,  # Speed of the speech (1.00 is normal speed)
        "loudness": 1.5,  # Volume/loudness adjustment (1.5 is amplified)
        "speech_sample_rate": 16000,  # Sample rate for the audio in Hz
        "enable_preprocessing": True,  # Preprocess text to clean or normalize it
        "model": "bulbul:v1"  # Model used for speech synthesis
    }

    # Set the request headers, including the API key from the environment variables
    headers = {
        "Content-Type": "application/json",  # Specifying content type as JSON
        "API-Subscription-Key": os.environ['SARVAM_API_KEY']  # API key loaded from .env
    }

    # A POST request to the Text-to-Speech API with the provided payload and headers
    response = requests.request("POST", url, json=payload, headers=headers).json()

    # The API response contains a list of base64-encoded audio segments
    audio_raw = ''.join(response['audios'])  # Concatenate all audio segments

    # Decode the base64 audio data into binary WAV format
    decoded_audio = base64.b64decode(audio_raw)

    # Create an in-memory file-like object (BytesIO) to hold the decoded audio data
    audio_buffer = io.BytesIO(decoded_audio)

    # Return the in-memory audio buffer to be used in the app
    return audio_buffer
