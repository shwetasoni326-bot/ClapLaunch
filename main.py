import os
import time
import numpy as np
import pyaudio

# Audio Configuration
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
THRESHOLD = 30000
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Listening for claps... Press Ctrl+C to stop.")

try:
    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        audio_data = np.frombuffer(data, dtype=np.int16)
        peak = np.abs(audio_data).max()
        
        if peak > THRESHOLD:
            print(f"Clap Detected! Volume Peak: {peak}")
            time.sleep(1)

except KeyboardInterrupt:
    print("\nStopping listener...")
    stream.stop_stream()
    stream.close()
    p.terminate()