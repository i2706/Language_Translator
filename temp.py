#Speech recognition lib
import speech_recognition as sr
#speech narration lib
import pyttsx3 as pt
#Speech Translation or text Translation lab
from translate import Translator
r = sr.Recognizer()

def Speak(command):
    engine = pt.init()
    #engine.setProperty("language",'hi')
    engine.say(command)
    engine.runAndWait()
    
with sr.Microphone(device_index=1) as s2:
    print("kindly speak")
    r.adjust_for_ambient_noise(s2,duration =1)
    r.pause_threshold=2
    a2 = r.listen(s2,timeout=5,phrase_time_limit=5)
    #audio=r.record(s2)
    #a2 = r.listen(s2)
    print("stop")
    try:
        txt = r.recognize_google(a2)
        txt = txt.lower()
        print("did you say "+txt)
        tran = Translator(to_lang='spanish')
        trans = tran.translate(txt)
        Speak("In spanish")
        print(trans)
        Speak(trans)
    except:
        print("error")