from coach_agent import generate_response
from tts import speak
import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"❌ Speech Recognition error: {e}")
        return ""

def main():
    print("🎙️ Welcome to your offline self-coach! Say 'exit' to quit.\n")

    while True:
        user_input = listen()  # 🧠 Voice input instead of keyboard

        if user_input.lower() in ['exit', 'quit']:
            break

        if not user_input.strip():
            continue  # Ignore empty speech

        response = generate_response(user_input)
        print("🤖 Coach:", response)
        speak(response)  # 🗣️ AI speaks the answer

if __name__ == "__main__":
    main()
