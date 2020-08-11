import pyttsx3

data = input("enter text which you want to hear\n")
engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()
