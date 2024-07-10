from vosk import Model,KaldiRecognizer
import pyaudio

model = Model("D:\\Code\\MARK\\Voice model\\vosk-model-small-en-us-0.15")

recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(rate=16000,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)
    if len(data) == 0:
        print("mic not working")
        break
    if recognizer.AcceptWaveform(data):
        print(recognizer.Result())





