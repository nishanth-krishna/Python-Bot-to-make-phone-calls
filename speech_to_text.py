import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:

    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")

textme = text
if 'Jarvis' in textme:
    print('hello sir')
    print('how can i help you, sir')