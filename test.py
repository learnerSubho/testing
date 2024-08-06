import pyttsx3
import wikipedia
voice = pyttsx3.init()
voices = voice.getProperty('voices')
voice.setProperty('voice',voices[1].id)
In = input("Enter the prompt: ")
# Line = int(input("Enter the number of line you want to see: "))
result = wikipedia.summary(In ,sentences= 10)
print(result)
voice.say(result)
voice.runAndWait()