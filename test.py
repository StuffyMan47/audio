import pyaudio
import wave
import fastapi
from fastapi import FastAPI, UploadFile
from fastapi.responses import HTMLResponse

# Данная программа записывает речь с помощью микрофона и сохраняет в формате .wav

CHUNK = 1024 # определяет форму аудио сигнала
FRT = pyaudio.paInt16 # шестнадцатибитный формат задает значение амплитуды
CHAN = 1 # канал записи звука
RT = 44100 # частота
REC_SEC = 5 #длина записи
OUTPUT = "output.wav"

p = pyaudio.PyAudio()
# format - шестнадцатибитный формат задает значение амплитуды, канал записи звука, rate - частота, fpb - определяет форму аудио сигнала
stream = p.open(format=FRT, channels=CHAN, rate=RT, input=True, frames_per_buffer=CHUNK) # открываем поток для записи

print("rec")
frames = [] # формируем выборку данных фреймов
for i in range(0, int(RT / CHUNK * REC_SEC)):
    data = stream.read(CHUNK)
    frames.append(data)
print("done")
stream.stop_stream() # останавливаем и закрываем поток
stream.close()
p.terminate()

w = wave.open(OUTPUT, 'wb')
w.setnchannels(CHAN)
w.setsampwidth(p.get_sample_size(FRT))
w.setframerate(RT)
w.writeframes(b''.join(frames))
w.close()
