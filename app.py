from rag_pipeline import ask_question
from speech_to_text import listen_to_user
from text_to_speech import speak_text

print("🎤 Voice RAG AI Assistant started")
print("Say 'exit' to stop\n")

while True:

    question = listen_to_user()

    if question is None:
        continue

    if "exit" in question.lower():
        print("Goodbye!")
        speak_text("Goodbye!")
        break

    answer = ask_question(question)

    speak_text(answer)