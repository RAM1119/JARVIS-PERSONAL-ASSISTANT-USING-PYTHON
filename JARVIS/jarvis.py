from urllib.parse import quote
import speech_recognition as ck
import wikipedia
import pyttsx3
import webbrowser
import os
import datetime
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def aus():
    r=ck.Recognizer()
    with ck.Microphone() as src:
        print("Listening....")
        audio=r.listen(src)
        said=""
        
        try:
            said=r.recognize_google(audio)
            print(said)
            speak(said)
        except Exception as fo:
            print(str(fo)+"is error")
    return said

def sendmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yourmail','password')
    server.sendmail('yourmail',to,content)
    server.close()

if __name__=='__main__':
    speak('im your assistant,please tell me hom may i help you')
    while True:
        query=aus().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            print('searching wikipedia...')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak("According To Wikipedia..")
            print("According To Wikipedia..")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'play music' in query:
            music_dir='E:\\songs' #type your pc preferred path
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak("the time is")
            speak(strTime)
            print("The Time is: "+str(strTime))
        
        elif 'open code' in query:
            codepath="C:\\Users\\91818\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" #choose your preferred path of your pc
            os.startfile(codepath)
        
        elif 'email to nameoftheperson to whom your sending' in query:
            try:
                speak("what should i say")
                content=aus()
                to='mail of the person you need to send'
                sendmail(to,content)
                speak("Email Sent!")
                print("Email Sent!")
            except Exception as e:
                #print(e)
                print("Sorry I Cant Send!")
                speak("Sorry I Cant Send!")    

        elif 'stop' in query:
            print('Thank You,Have a Nice Day')
            speak("Thank You,Have a Nice Day")
            break

