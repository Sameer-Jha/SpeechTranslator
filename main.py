import speech_recognition as sr
import pyttsx3 as tts
from modules.audio_engine import Audio_Engine
from modules.translation_engine import Translation_Engine

def main():

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    ttsengine = tts.init()
    language1 = input('Enter the source language: ')
    language2 = input('Enter the output language: ')

    print("Initializing processing engines")
    try:
        audioEngine = Audio_Engine(recognizer, microphone, ttsengine)
        translationEngine = Translation_Engine(language1.lower(), language2.lower())
        
        print('\nConversation starts....\n')

        try:
            while True:
                data = audioEngine.recognize_speech_from_mic()
                if data['success'] == True and data['transcription'] != None:
                    print(f"I heard: {data}\nTranslating..\n")
                    translated_data = translationEngine.translate(data['transcription'])
                    print(translated_data)
                    audioEngine.speak(translated_data)
                else:
                    print(f"\n\nError Occured:\n{data['error']}")

        except KeyboardInterrupt:
            print('Program terminated by user\n')

    except Exception as e:
        print(f"Error occured in engine initilaization: {e}")

    
if __name__ == "__main__":
    main()