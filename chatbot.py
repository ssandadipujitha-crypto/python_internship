# Basic Chatbot

print("Hello! I am a simple chatbot.")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hi! How are you?")

    elif user_input == "how are you":
        print("Bot: I'm fine, thank you!")

    elif user_input == "what is your name":
        print("Bot: My name is Python Chatbot.")

    elif user_input == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")