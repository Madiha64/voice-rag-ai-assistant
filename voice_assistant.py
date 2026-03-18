import speech_recognition as sr
import pyttsx3
import ollama

# speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print("You:", query)
        return query

    except:
        print("Sorry, could not understand.")
        return ""


def run_voice_assistant():

    print("Voice Assistant Started. Say 'exit' to stop.")

    while True:

        query = listen()

        if query == "":
            continue

        if "exit" in query.lower():
            speak("Goodbye")
            break

        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": query}]
        )

        answer = response["message"]["content"]

        print("AI:", answer)

        speak(answer)


if __name__ == "__main__":
    run_voice_assistant()