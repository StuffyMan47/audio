from vosk import Model, KaldiRecognizer
import os, json
import pyaudio

# Данная программа переводит речь в текст с помощью микрофона

if not os.path.exists("Smodel"):
    print("please download the model from https://alphacephei.com/vosk/models")
    exit(1)

model = Model("Smodel")
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
# format - шестнадцатибитный формат задает значение амплитуды, канал записи звука, rate - частота, fpb - определяет форму аудио сигнала
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        x = json.loads(rec.Result())
        print(x["text"])

    else:
        #print(rec.PartialResult())
        pass

print(rec.FinalResult())