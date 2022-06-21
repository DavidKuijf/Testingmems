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
    
def fft_calc(data_vec):
    data_vec = data_vec*np.hanning(len(data_vec)) # hanning window
    N_fft = len(data_vec) # length of fft
    freq_vec = (float(CHUNK)*np.arange(0,int(N_fft/2)))/N_fft # fft frequency vector
    fft_data_raw = np.abs(np.fft.fft(data_vec)) # calculate FFT
    fft_data = fft_data_raw[0:int(N_fft/2)]/float(N_fft) # FFT amplitude scaling
    fft_data[1:] = 2.0*fft_data[1:] # single-sided FFT amplitude doubling
    return freq_vec,fft_data

for i in range(0, 10):
    data = stream.read(CHUNK)
    frames.pop()
    frames.appendleft(data)
    np.frombuffer(data, dtype=np.int16)
    print(fft_calc(data))

stream.stop_stream()
stream.close()

p.terminate()