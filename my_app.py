import pyttsx3 
import speech_recognition as sr




def speak_out( talk ):
    converter = pyttsx3.init() 

    converter.setProperty('rate', 150) 

    converter.setProperty('volume', 0.7) 

    voice_id = "com.apple.speech.synthesis.voice.samantha"


    converter.setProperty('voice', voice_id) 

    converter.runAndWait() 


    converter.say(talk) 
    #converter.say("How can i help you") 

    converter.runAndWait() 






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

    speak_out("Hello, How can i help you")

    with sr.Microphone() as source:

        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize what you said")

        textmeagain = text
        if 'call Krishna' in textmeagain:

                speak_out("Calling Krishna in a moment")

                






