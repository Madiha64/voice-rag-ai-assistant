import speech_recognition as sr

def listen_to_user():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak your question...")
        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text

    except sr.UnknownValueError:
        print(" Could not understand audio")
        return None

    except sr.RequestError:
        print(" Speech recognition service error")
        return None