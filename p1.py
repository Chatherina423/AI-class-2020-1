import speech_recognition as sr

r1 = sr.Recognizer()
r2 = sr.Recognizer()

havard = sr.AudioFile('harvard.wav')
jackhammer = sr.AudioFile('jackhammer.wav')

with havard as source:
    audio1 = r1.record(source, offset=4, duration=3)

print(type(audio1))
print(r1.recognize_google(audio1))

with jackhammer as source:
    r2.adjust_for_ambient_noise(source, duration=0.5)
    audio2 = r2.record(source)

print(r2.recognize_google(audio2))