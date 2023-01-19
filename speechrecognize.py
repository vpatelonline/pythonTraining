import speech_recognition as sr

r = sr.Recognizer()
myaudio = sr.AudioFile('D:\IT\Python\happybirtday.wav')

with myaudio as source:

 audio = r.record(source)
 print(type(audio))

 print(r.recognize_google(audio))
