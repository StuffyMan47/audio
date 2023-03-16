import wave
import shutil
from vosk import Model, KaldiRecognizer
import os, json

# Данная программа проверяет чтение файла .wav

def listen():
    model = Model("Smodel")
    rec = KaldiRecognizer(model, 44100)
    wf = wave.open(r'output.wav', "rb")
    last_n = False
    result = ''
    while True:
        data = wf.readframes(44100)
        if len(data) == 0:
            break

        if rec.AcceptWaveform(data):
            x = json.loads(rec.Result())
            result = x["text"]
        else:
            pass
    return(result)

print(listen())