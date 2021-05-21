import speech_recognition as sr
import pyttsx3 as tts

class Audio_Engine:

    def __init__(self, recognizer, microphone, tts_engine):
        self.recognizer = recognizer
        self.microphone = microphone
        self.ttsengine = tts_engine

    def recognize_speech_from_mic(self):
        """Transcribe speech from recorded from `microphone`.

        Returns a dictionary with three keys:
        "success": a boolean indicating whether or not the API request was
                successful
        "error":   `None` if no error occured, otherwise a string containing
                an error message if the API could not be reached or
                speech was unrecognizable
        "transcription": `None` if speech could not be transcribed,
                otherwise a string containing the transcribed text
        """

        recognizer = self.recognizer
        microphone = self.microphone

        # check that recognizer and microphone arguments are appropriate type
        if not isinstance(recognizer, sr.Recognizer):
            raise TypeError("`recognizer` must be `Recognizer` instance")

        if not isinstance(microphone, sr.Microphone):
            raise TypeError("`microphone` must be `Microphone` instance")

        # adjust the recognizer sensitivity to ambient noise and record audio
        # from the microphone
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        # set up the response object
        response = {
            "success": True,
            "error": None,
            "transcription": None
        }

        # try recognizing the speech in the recording
        # if a RequestError or UnknownValueError exception is caught,
        #     update the response object accordingly
        try:
            response["transcription"] = recognizer.recognize_google(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            # speech was unintelligible
            response["error"] = "Unable to recognize speech"

        return response

    def speak(self, response):
        if response['success'] == True and response['transcription'] != None:
            engine = self.ttsengine
            engine.say(response['transcription'])
            engine.runAndWait()
        else:
            print(f"\n\nError Occured:\n{response['error']}")
        


def main():
    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    ttsengine = tts.init()
    audio = Audio_Engine(recognizer, microphone, ttsengine)
    recording = audio.recognize_speech_from_mic()
    print(recording)
    audio.speak(recording)


if __name__ == "__main__":
    main()
