"""
PyAudio Example: Make a wire between input and output (i.e., record a
few samples and play them back immediately).
"""

import pyaudio
import numpy as np
import wave
from collections import deque

CHUNK = 44100
FORMAT = pyaudio.paInt16
WIDTH = 2
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5


p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

frames = deque([0,0,0,0,0,0,0,0,0,0])

for i in range(0, 10):
    data = stream.read(CHUNK)
    frames.pop()
    frames.appendleft(data)
    print(np.frombuffer(data, np.int16))


stream.stop_stream()
stream.close()

p.terminate()