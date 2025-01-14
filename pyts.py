import pyttsx3
from whisper_test import result
engine = pyttsx3.init()

rate = engine.getProperty('rate')
print(rate)
# engine.setProperty('rate',125)

volume = engine.getProperty('volume')
print(volume)
# engine.setProperty('volume',1.0)

voices = engine.getProperty('voices')
# Engine.setProperty('voice',voices[1].id) 1 for female 


engine.say(result["text"])
engine.runAndWait()
engine.stop()

# engine.save_to_file(result[text],'test.mp3')
# engine.runAndWait()