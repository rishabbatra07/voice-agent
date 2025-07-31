import gradio as gr
from coach_agent import generate_response
from tts import speak
from whisper_input import transcribe_audio

chat_history = []

def chat_with_agent(audio_input=None, text_input=""):
    global chat_history

    # Handle input priority: audio > text
    if audio_input:
        try:
            user_text = transcribe_audio(audio_input)
        except Exception as e:
            return f"⚠️ Error transcribing audio: {e}"
    else:
        user_text = text_input.strip()

    if not user_text:
        return "🤖 Please speak or type something."

    chat_history.append(("You", user_text))

    try:
        response = generate_response(user_text)
    except Exception as e:
        response = f"⚠️ Error generating response: {e}"

    chat_history.append(("Coach", response))

    # Optional TTS
    try:
        speak(response)
    except Exception as e:
        print(f"[TTS ERROR] {e}")

    # Display conversation
    conversation = "\n\n".join(f"**{sender}:** {msg}" for sender, msg in chat_history)
    return conversation

# Build UI
with gr.Blocks()
