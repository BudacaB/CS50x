import speech_recognition
import re

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say something")
    audio = recognizer.listen(source)

# print("Google Speech Recognition thinks you said:")
# print(recognizer.recognize.google(audio))

words = recognizer.recognize_google(audio)

matches = re.search("my name is (.*)", words)
if matches:
    print(f"Hey, {matches[1]}")
else:
    print("Hey, you")