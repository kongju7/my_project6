import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source) 
        print("음성 인식 대기중")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language = "ko")
        return text 
    except sr.UnknownValueError:
        print("인식할 수 없습니다.")
    except sr.RequestError as e:
        print("인식에 문제가 있습니다.", e)


if __name__ == "__main__":
    recognize_speech()