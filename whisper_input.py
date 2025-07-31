# from faster_whisper import WhisperModel
# import sounddevice as sd
# import numpy as np
# import tempfile
# import scipy.io.wavfile as wav
#
# # Load Whisper model (CPU)
# model = WhisperModel("base", device="cpu", compute_type="int8")
#
# def listen():
#     duration = 5  # seconds
#     fs = 16000    # sampling frequency
#     print("🎤 Listening for 5 seconds...")
#
#     recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
#     sd.wait()
#
#     # Save to a temporary WAV file
#     with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
#         wav.write(temp_audio.name, fs, recording)
#
#         print("🧠 Transcribing...")
#         segments, _ = model.transcribe(temp_audio.name)
#         result = "".join([segment.text for segment in segments])
#
#         print("🗣️ You said:", result)
#         return result
# whisper_input.py

from faster_whisper import WhisperModel
import sounddevice as sd
import numpy as np
import tempfile
import scipy.io.wavfile as wav

# Load Whisper model once
model = WhisperModel("base", device="cpu", compute_type="int8")

def transcribe_audio(audio_path=None):
    """
    If audio_path is provided (from Gradio), transcribe it.
    If not, record from mic for 5 seconds.
    """
    if audio_path:
        segments, _ = model.transcribe(audio_path)
    else:
        # Record from mic
        duration = 5  # seconds
        fs = 16000    # sampling frequency
        print("🎤 Listening for 5 seconds...")

        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
            wav.write(temp_audio.name, fs, recording)
            segments, _ = model.transcribe(temp_audio.name)

    result = "".join([segment.text for segment in segments])
    print("🗣️ You said:", result)
    return result
