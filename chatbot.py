# Simple Q&A Chatbot
# This chatbot runs in the terminal and responds to basic greetings and questions.

def chatbot():
    print("Bot: Hello! Type 'exit' to end the chat.\n")

    while True:
        user_input = input("User: ").lower()

        if user_input == "exit":
            print("Bot: Goodbye!")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("Bot: Hello there!")

        elif "good morning" in user_input:
            print("Bot: Good morning! How are you doing today?")

        elif "how are you" in user_input:
            print("Bot: I am doing very well, thank you for asking.")

        elif "your name" in user_input:
            print("Bot: I am a simple Python chatbot created for an AI assignment.")

        else:
            print("Bot: That's interesting! Tell me more.")


if __name__ == "__main__":
    chatbot()