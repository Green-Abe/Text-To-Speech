"""Text To Speech Talker a,n example program using the text-to-speech features of the pyttsx3
module.
"""
import sys

try:
    import pyttsx3
except ImportError:
    print('The pyttsx3 module needs to be installed to run this')
    print('program. On Windows, open a Command Prompt and run:')
    print('pip install pyttsx3')
    print('On macOS and Linux, open a Terminal and run:')
    print('pip3 install pyttsx3')
    sys.exit()

tts = pyttsx3.init()  # Initialize the TTS engine.

print('Text To Speech Talker')
print('Text-to-speech using the pyttsx3 module, which in turn uses')
print('the NSSpeechSynthesizer (on macOS), SAPI5 (on Windows), or')
print('eSpeak (on Linux) speech engines.')
print()
print('Enter the text to speak, or QUIT to quit.')

while True:
    text = input('> ')
    
    if text.upper()=='CHANGE VOICE':
        engine=pyttsx3.init()
        voices = engine.getProperty('voices')       #getting details of current voice
        print('voice index is even 0 or 1')
        VA=int(input("enter a voice index :"))
        print(type(VA))
        if VA > 1 or VA < 0 :
            print("voice index is even 1 or 0")
            sys.exit()
        engine.setProperty('voice', voices[VA].id)  #changing index, changes voices. o for male
        #engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female
        


  

    if text.upper()=='CHANGE RATE':
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')   # getting details of current speaking rate
        print (rate)                        #printing current voice rate
        engine.setProperty('rate', 125)
        RA=int(input("ente a rate :"))     # setting up new voice rate
        engine.setProperty('rate', RA)

    if text.upper() == 'QUIT':
        print('Thanks for playing!')
        sys.exit()

    tts.say(text)  # Add some text for the TTS engine to say.
    tts.runAndWait()  # Make the TTS engine say it.

    

