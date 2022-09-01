# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 13:35:44 2022

@author: Oran Nahum
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 12:39:53 2022

@author: Oran Nahum
"""

import pyaudio
import wave
import os
#import tensorflow_io as tfio
import tensorflow as tf 
from turtle_helper import move_turtle, starting_frame, not_snoring_detection
from audio_processing import load_mp3_16k_mono,preprocess_mp3
CHANK = 1024    
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
i=0

last_command = 0
starting_frame()

model = tf.keras.models.load_model('./saved_models/my_h5_model.h5')



for i in range (0,20):
    if i==0:
        not_snoring_detection()
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHANK)
    
    
    print(f"Start Recording{i} ...")
    i=+1
    frames = []
    seconds = 1.021679
    
    for i in range(0, int(RATE / CHANK * seconds)):
        data = stream.read(CHANK)
        frames.append(data)
        
    print("recording stopped!")
    
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    
    wf = wave.open("output.mp3", "wb")   
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    
    
    wf.close()  
    
    mp3 = os.path.join('output.mp3')
    wav = load_mp3_16k_mono(mp3)
    audio_slices = tf.keras.utils.timeseries_dataset_from_array(wav, wav, sequence_length=16000, sequence_stride=16000, batch_size=1)
    samples, index = audio_slices.as_numpy_iterator().next()
    audio_slices = tf.keras.utils.timeseries_dataset_from_array(wav, wav, sequence_length=16000, sequence_stride=16000, batch_size=1)
    audio_slices = audio_slices.map(preprocess_mp3)
    audio_slices = audio_slices.batch(64)
    yhat = [1 if prediction > 0.99 else 0 for prediction in model.predict(audio_slices)]
    command = yhat[0]

    move_turtle(command,last_command)
    if yhat[0] == 1:
        print("Snoring")
    elif  yhat[0] == 0:
        print("Not Snoring")
    
    last_command = command
