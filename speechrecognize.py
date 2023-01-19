import speech_recognition as sr

r = sr.Recognizer()
myaudio = sr.AudioFile('D:\IT\Python\happybirtday.wav')

with myaudio as source:

# For full audio to text
    #audio = r.record(source)
 
# For audio to text up to 1 second - gives error
    #audio = r.record(source, duration=1)

# For audio to text up to 2 seconds - It works
    #audio = r.record(source, duration=1)  

# skip first 0.9 second and print text up to next 2 seconds?
    audio = r.record(source, offset=0.9, duration=2)  

    print(type(audio))

    print(r.recognize_google(audio))
