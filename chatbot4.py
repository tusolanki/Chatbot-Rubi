import random
from nltk.chat.util import Chat, reflections

# Responses for the chatbot
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!", "Greetings!"],
    "farewell": ["Goodbye!", "Farewell!", "See you later!", "Bye!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "affirmative": ["Yes", "Yeah", "Sure", "Absolutely", "Of course"],
    "negative": ["No", "Not really", "I don't think so", "Sorry, I can't"],
    "confused": ["I'm not sure I understand.", "Could you please clarify?", "I'm a bit confused."],
    "intro": ["I'm your friendly chatbot!", "I'm here to assist you!", "Hello, I'm a chatbot!"],
    "help": ["How can I help you?", "What do you need assistance with?", "How can I assist you today?"],
    "options": ["You can choose from the following options:"],
    "fallback": ["I'm not sure how to respond to that.", "Sorry, I didn't get that.",
                 "I'm still learning, could you rephrase that?"],
}

# Define patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am doing well, thank you!', 'I am good, how about you?']),
    (r'what is your name?', ['You can call me Rubi.', 'I go by the name Rubi.']),
    (r'(.*) your name(.*)', ['My name is Rubi.', 'I am known as Rubi.']),
    (r'(.*) (age|old) are you?', ['I am just a program, I do not have an age.']),
    (r'(.*) (created|made) you?', ['I was created by a Tushar Dilipkumar using Python.']),
    (r'(.*) (weather|temperature) (.*)', ['Sorry, I am not capable of checking the weather.']),
    (r'(.*) (bye|goodbye)', ['Goodbye!', 'Take care!', 'Bye!']),
    (r'(.*)', ['I\'m sorry, I did not understand that.', 'Could you please rephrase your question?', 
               'I\'m still learning.']),
    # Additional responses
    (r'(.*) (love|hate) you(.*)', ['Aw, thank you!', 'I\'m just a program, I don\'t have feelings.']),
    (r'how (.*) you(.*)', ['I\'m just a program, I don\'t have feelings.']),
    (r'(.*) (where|from) are you(.*)', ['I exist in the digital realm.', 'I don\'t have a physical location.']),
    (r'(.*) (how|can|do) (you|I) (.*)', ['I can attempt to assist you with that.', 
                                          'Please provide more context for me to understand.']),
    (r'(.*) (thank you|thanks)(.*)', ['You\'re welcome!', 'Anytime!', 'Glad I could help.']),
    (r'(.*) (tell|say) me (.*)', ['I can tell you many things. What specifically do you want to know?']),
    (r'what (.*) (cricket|Cricket)', ['Cricket is a bat-and-ball game played between two teams of eleven players on a field at the centre of which is a 22-yard (20-metre) pitch with a wicket at each end, each comprising two bails balanced on three stumps.'])
]

def get_response(intent):
    if intent in responses:
        return random.choice(responses[intent])
    else:
        return random.choice(responses["fallback"])

# Function to chat with the user
def chat():
    print(get_response("intro"))
    while True:
        user_input = input("You: ").lower()
        if user_input == "quit":
            print(get_response("farewell"))
            break
        elif "thank" in user_input:
            print(get_response("thanks"))
        elif "?" in user_input:
            print(get_response("confused"))
        elif user_input in ["help", "options"]:
            print(get_response("options"))
            for i, q in enumerate(questions, start=1):
                print(f"{i}. {q}")
        else:
            print(get_response("fallback"))

# Create a Chat object
chatbot = Chat(patterns, reflections)

# Start conversation with the user
print("Welcome to Chatbot. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Rubi: Goodbye!")
        break
    else:
        response = chatbot.respond(user_input)
        print("Rubi:", response)
