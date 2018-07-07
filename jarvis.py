import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
 
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`

        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
def jarvis(data):
    if "how are you" in data:
        speak("I am fine")
 
    if "what time is it" in data:
       	speak(ctime())

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Manu, I will show you where " + location + " is.")
        os.system("firefox https://www.google.nl/maps/place/" + location + "/&amp;")
        
    if "what is the meaning of" in data:
        data = data.split()
        wordcount = len(data)
        print (wordcount)
        word = data[wordcount-1]
        speak("Wait Manu i will tell you the meaning of"+ word + " ")
        os.system("firefox www.dictionary.com/browse/" + word + "/&amp;")   
 
# initialization
time.sleep(2)
speak("Hi Manu, what can I do for you?")
def mainJarvis():
	data = recordAudio()
	jarvis(data)
	return data
if __name__ == "__main__":
	mainJarvis()
