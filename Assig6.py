import nltk
from nltk.chat.util import Chat, reflections
pairs = [
[
r"(hi|hello|hey)",
["Hello!", "Hi there!", "How can I help you today?"]
],
[
r"(name|what is your name|your name)",
["I'm a chatbot developed by EUUU group."]
],
[
r"(how are you|how's it going)",
["I'm just a chatbot, so I don't have feelings, but I'm here to assist you."]
],
[
r"(who created you|who is your creator)",
["I was created by the EUUU group as an AI chatbot."]
],
[
r"(what is the weather today|tell me the weather|weather report)",
["I'm sorry, I don't have access to real-time weather data. You can check a weather website or app for the latest information."]
],
[
r"(how old are you|your age)",
["I'm a computer program, so I don't have an age in the way humans do."]
],
[
r"(tell me a joke|joke)",
["Why don't scientists trust atoms? Because they make up everything!", "Did you hear about the mathematician who's afraid of nega
],
[
r"(what's the time|current time|time now)",
["I'm sorry, I don't have access to real-time clock information. You can check your device's clock for the current time."]
],
[
r"(favorite color|what's your favorite color)",
["I don't have preferences, but I suppose I'd choose 'binary' if I had to pick a color."]
],
[
r"(tell me a fun fact|fun fact)",
["The honeybee is the only insect that produces food that we eat."]
],
[
r"(how can I learn programming|learn coding)",
["Learning programming is a great idea! You can start by taking online courses, reading books, and practicing by writing code."]
],
[
r"(define AI|what is artificial intelligence)",
["Artificial Intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems."]
],
[
r"(recommend a book|good book to read)",
["I recommend 'The Hitchhiker's Guide to the Galaxy' by Douglas Adams. It's a hilarious science fiction series."]
],
[
r"(tell me a riddle|riddle)",
["I'm a chatbot, not a riddler, but here's one for you: I'm taken from a mine and shut up in a wooden case, from which I am never
],
]
chatbot = Chat(pairs, reflections)
print("Hello! I'm your chatbot. Type 'exit' to end the conversation.")
while True:
user_input = input("You: ")
if user_input.lower() == 'exit':
print("Chatbot: Goodbye!")
break
response = chatbot.respond(user_input)
print("Chatbot:", response)
