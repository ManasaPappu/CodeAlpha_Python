import string

def run():
    print("Chatbot started! Type something...")
    while True:
        response = input("> ").lower()
        # remove punctuation from the user message
        response = response.translate(str.maketrans('', '', string.punctuation))

        if response in ["hi", "hello", "hey"]:
            print("Hello!")
        elif response == "how are you":
            print("I'm fine, what about you?")
        elif response == "what are you doing":
            print("I'm currently chatting with you.")
        elif response in ["bye", "goodbye", "see you later", "catch you soon"]:
            print("Bye! Have a nice day!")
            break
        else:
            print("I don't understand. Please try again.")

run()
