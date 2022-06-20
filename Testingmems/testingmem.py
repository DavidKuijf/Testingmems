"""
PyAudio Example: Make a wire between input and output (i.e., record a
few samples and play them back immediately).
"""

import pyaudio

CHUNK = 44100
WIDTH = 2
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)


for i in range(0, 10):
    data = stream.read(CHUNK)
    print(int.from_bytes(data))



stream.stop_stream()
stream.close()

p.terminate()