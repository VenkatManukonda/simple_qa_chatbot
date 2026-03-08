# Simple Q&A Chatbot
# This chatbot runs in the terminal and responds to common greetings and questions.

responses = {
    "hello": "Hello there!",
    "hi": "Hi! How are you?",
    "good morning": "Good morning! How are you doing today?",
    "how are you": "I am doing very well, thank you for asking.",
    "your name": "I am a simple Python chatbot created for an AI assignment.",
    "bye": "Goodbye! Have a nice day."
}

def chatbot():
    print("Bot: Hello! Type 'exit' to end the chat.\n")

    while True:
        user_input = input("User: ").lower()

        if user_input == "exit":
            print("Bot: Goodbye!")
            break

        # Check if user input matches a key in responses
        matched = False
        for key in responses:
            if key in user_input:
                print("Bot:", responses[key])
                matched = True
                break

        if not matched:
            print("Bot: That's interesting! Tell me more.")

if __name__ == "__main__":
    chatbot()
