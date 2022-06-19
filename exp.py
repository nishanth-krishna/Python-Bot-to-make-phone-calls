import pyttsx3 
import speech_recognition as sr

from twilio.rest import Client



def jarvis_says( talk ):
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

    jarvis_says("Hello, How can i help you")

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

                jarvis_says("Calling Krishna in a moment")


                account_sid = 'ACc7df3cbbd2bf9a13174217041dc2a196'
                auth_token = '0e0586de7930abf31ac7e2b3bd397c08'
                client = Client(account_sid, auth_token)

                call = client.calls.create(
                        twiml='<Response><Say>Hi Krishna, this is your smart assistant</Say></Response>',
                        to='+917989658774',
                        from_='+12067361389'
                    )

                print(call.sid)

        elif 'call Jyoti' in textmeagain:

                jarvis_says("Calling Jyoti in a moment")


                account_sid = 'ACc7df3cbbd2bf9a13174217041dc2a196'
                auth_token = '0e0586de7930abf31ac7e2b3bd397c08'
                client = Client(account_sid, auth_token)

                call = client.calls.create(
                        twiml='<Response><Say>Hi Krishna, this is E.D.I.T.H, your smart assistant</Say></Response>',
                        to='+919949418372',
                        from_='+12067361389'
                    )

                print(call.sid)        

        
        

                
                






