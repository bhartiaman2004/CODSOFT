# Very Simple Rule-Based Chatbot

def chatbot():
    print("Chatbot: Hello! How can I help you?")

    while True:
        # Get user input
        user_input = input("You: ").lower()

        # Basic responses
        if user_input == "hello":
            print("Chatbot: Hi there!")
        
        elif user_input == "how are you":
            print("Chatbot: I'm good! How are you?")
        
        elif user_input == "what's your name":
            print("Chatbot: I'm just a simple chatbot.")
        
        elif user_input == "what can you do":
            print("Chatbot: I can respond to simple messages!")
        
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break  # End the chat
        
        else:
            print("Chatbot: I don't understand that. Try something else.")

# Run the chatbot
chatbot()