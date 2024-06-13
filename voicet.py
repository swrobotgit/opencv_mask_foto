import vosk
import sys
import os
import pyaudio

model = vosk.Model("vosk-model-small-ru-0.22")
rec = vosk.KaldiRecognizer(model, 16_000)

def recognize():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16_000, input=True, frames_per_buffer=8_000)
    while 1:
        data = stream.read(300)
        if len(data) == 0: break
        if rec.AcceptWaveform(data):
            result = rec.Result()
            print(result)
            if "ярослав" in result or "ярик" in result or "йарик" in result or "жорик" in result:
                return "yarik+90"
            if "матата" in result or "обезьяна" in result or "макака" in result:
                return "makaka+75"
            if "шрек" in result or "шрэк" in result or "ширак" in result:
                return "shrek+75"


while True:
    rez = recognize()
    with open("who.txt", "w") as w:
        w.write(rez)
        w.close()
