import speech_recognition as sr

r = sr.Recognizer()
myaudio = sr.AudioFile('D:\IT\Python\happybirtday.wav')

with myaudio as source:

 audio = r.record(source)   # For full audio to text
 #audio = r.record(source, duration=1)  - For audio to text up to 1 second - gives error.
 #audio = r.record(source, duration=1)  - For audio to text up to 2 seconds - It works.
 print(type(audio))

 print(r.recognize_google(audio))
