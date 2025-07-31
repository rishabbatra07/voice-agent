# tts.py
import pyttsx3

def speak(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 180)   # Adjust speed if needed
        engine.setProperty('volume', 1.0) # Max volume
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(f"[TTS ERROR] {e}")
