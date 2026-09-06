import os
import time
import numpy as np
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
THRESHOLD = 30000

CLAP_TIMEOUT = 1.0
clap_count = 0
last_clap_time = 0

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Listening for double claps... Press Ctrl+C to stop.")

try:
    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        audio_data = np.frombuffer(data, dtype=np.int16)
        peak = np.max(np.abs(audio_data))
        
        current_time = time.time()
        
        if clap_count > 0 and (current_time - last_clap_time) > CLAP_TIMEOUT:
            clap_count = 0

        if peak > THRESHOLD:
            if current_time - last_clap_time > 0.15:
                clap_count += 1
                last_clap_time = current_time
                print(f"Clap {clap_count} Detected! Volume Peak: {peak}")

                if clap_count == 2:
                    print("--> DOUBLE CLAP DETECTED! Opening YouTube...")
                    os.system("start https://www.youtube.com")
                    clap_count = 0
                    time.sleep(0.5)

except KeyboardInterrupt:
    print("Stopping listener...")

stream.stop_stream()
stream.close()
p.terminate()