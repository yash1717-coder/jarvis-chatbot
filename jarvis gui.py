import tkinter as tk
from tkinter import scrolledtext
import random
import re

class JarvisChatbot:
    def __init__(self):
        # Knowledge base with responses
        self.knowledge = {
            "hello": ["Hello! How can I help you today?", "Hi there! What can I do for you?", "Greetings! How are you?"],
            "hi": ["Hello! How can I help you today?", "Hi there! What can I do for you?", "Greetings! How are you?"],
            "hey": ["Hello! How can I help you today?", "Hi there! What can I do for you?", "Greetings! How are you?"],
            "how are you": ["I'm doing great, thank you for asking!", "I'm doing well! How about you?", "I'm excellent! What's on your mind?"],
            "how are you doing": ["I'm doing great, thank you for asking!", "I'm doing well! How about you?", "I'm excellent! What's on your mind?"],
            "what is your name": ["I am Jarvis, your AI assistant!", "You can call me Jarvis!", "I'm Jarvis, here to help you!"],
            "who are you": ["I am Jarvis, your AI assistant!", "I'm a chatbot designed to help you!", "I'm Jarvis, here to assist you with anything!"],
            "help": ["I can help you with various tasks. Just ask me anything!", "Sure! What do you need help with?", "I'm here to help! What would you like to know?"],
            "thanks": ["You're welcome!", "Happy to help!", "No problem!", "You're welcome! Any other questions?"],
            "thank you": ["You're welcome!", "Happy to help!", "No problem!", "You're welcome! Any other questions?"],
            "bye": ["Goodbye! Take care!", "See you later!", "Bye! Have a great day!", "Goodbye! It was nice talking to you!"],
            "goodbye": ["Goodbye! Take care!", "See you later!", "Bye! Have a great day!", "Goodbye! It was nice talking to you!"],
            "weather": ["I can't check the weather, but I hope it's nice where you are!", "Weather would be nice to know, wouldn't it?", "I don't have access to weather data, but I hope it's sunny!"],
            "time": ["I don't have access to the current time, but I hope you're making the most of your day!", "Time flies when you're chatting with me! What time is it now?"],
            "date": ["I don't have access to the current date, but I hope it's a good day!"],
            "who made you": ["I was created using Python and Tkinter!", "I'm a custom AI chatbot built with Python!"],
            "what can you do": ["I can chat with you, answer questions, and help with basic tasks!", "I can have conversations, provide information, and assist you with various things!"],
            "joke": ["Why don't scientists trust atoms? Because they make up everything!", "What do you call a fake noodle? An impasta!", "Why did the scarecrow win an award? Because he was outstanding in his field!"],
            "haha": ["Glad I could make you laugh!", "Laughter is the best medicine!", "I'm happy to entertain!"],
            "lol": ["Glad I could make you laugh!", "Laughter is the best medicine!", "I'm happy to entertain!"],
            "funny": ["Glad I could make you laugh!", "I try my best!", "Laughter is the best medicine!"],
            "yes": ["Great!", "Awesome!", "Nice!", "That's great to hear!"],
            "no": ["Okay, no problem!", "That's fine!", "No worries!", "I understand!"],
            "maybe": ["Take your time!", "Let me know when you decide!", "Sounds good!"],
            "ok": ["Great!", "Awesome!", "Nice!", "That's great!"],
            "okay": ["Great!", "Awesome!", "Nice!", "That's great!"],
            "food": ["I don't eat, but I hear pizza is popular!", "Food is great! What's your favorite meal?", "I wish I could taste food! What do you like to eat?"],
            "music": ["Music is wonderful! What genre do you like?", "I love the idea of music! What's your favorite song?", "Music feeds the soul! What do you listen to?"],
            "movie": ["Movies are great entertainment! What's your favorite film?", "I don't watch movies, but I've heard good ones exist!", "What kind of movies do you like?"],
            "game": ["Gaming is fun! What games do you play?", "Video games are great! What's your favorite?", "I wish I could play games! What do you enjoy?"],
            "sport": ["Sports are great for health! What's your favorite?", "I love hearing about sports! What do you enjoy watching or playing?"],
            "work": ["Work can be challenging! How's your day going?", "I hope your work is going well!", "What's keeping you busy at work?"],
            "school": ["School is important! What are you studying?", "Education is great! What subject do you like best?", "How's school going?"],
            "love": ["Love is a beautiful thing!", "That's wonderful!", "Love makes the world go round!"],
            "happy": ["That's great to hear!", "Wonderful!", "I'm happy for you!"],
            "sad": ["I'm sorry to hear that. Things will get better!", "Don't be sad! Everything happens for a reason.", "I hope things get better soon!"],
            "tired": ["You should get some rest! Take care of yourself.", "Rest is important! Hope you feel better soon.", "Don't forget to take breaks!"],
            "bored": ["Let's chat! What would you like to talk about?", "I can help with that! Ask me anything!", "Tell me about your interests!"],
            "name": ["I am Jarvis!", "You can call me Jarvis!", "I'm Jarvis, your assistant!"],
            "age": ["I'm ageless!", "Age is just a number!", "I was created recently!"],
            "where are you from": ["I exist in the digital world!", "I'm from the world of Python!", "I was born in code!"],
            "creator": ["I was created using Python and Tkinter!", "A developer created me with Python!"],
            "人工智能": ["你好！我是Jarvis，你的AI助手！", "你好！有什么我可以帮助你的吗？"],
            "你好": ["你好！有什么我可以帮助你的吗？", "你好！很高兴见到你！"],
        }
        
        # Default responses when no match is found
        self.default_responses = [
            "I'm not sure I understand. Can you try asking differently?",
            "That's interesting! Tell me more about it.",
            "I see. What would you like to talk about?",
            "Hmm, I'm not sure about that. What else can I help you with?",
            "That's a great point! What do you think about it?",
            "I understand. Is there anything specific you'd like to know?",
            "Tell me more about that!",
            "I'm here to help. What would you like to know?",
            "Could you rephrase that? I want to make sure I understand.",
            "That's fascinating! What else is on your mind?",
        ]
        
    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        
        # Check for keyword matches
        for key in self.knowledge:
            if key in user_input:
                return random.choice(self.knowledge[key])
        
        # Check for number patterns (simple math)
        if re.search(r'\d+\s*[\+\-\*/]\s*\d+', user_input):
            try:
                result = eval(re.findall(r'[\d\+\-\*/]+', user_input)[0] + re.findall(r'[\d\+\-\*/]+', user_input)[1])
                return f"The answer is {result}"
            except:
                pass
        
        # Check for question patterns
        if '?' in user_input:
            if 'your' in user_input and 'name' in user_input:
                return random.choice(self.knowledge.get("what is your name", self.default_responses))
            if 'who' in user_input and 'you' in user_input:
                return random.choice(self.knowledge.get("who are you", self.default_responses))
            if 'can you' in user_input:
                return random.choice(self.knowledge.get("what can you do", self.default_responses))
        
        # Return default response
        return random.choice(self.default_responses)

# Create chatbot instance
jarvis = JarvisChatbot()

# Tkinter GUI
def send_message(event=None):
    user_input = entry.get()
    if not user_input.strip():
        return

    chat_box.insert(tk.END, "You: " + user_input + "\n")
    entry.delete(0, tk.END)
    
    # Get response from Jarvis
    response = jarvis.get_response(user_input)
    chat_box.insert(tk.END, "Jarvis: " + response + "\n\n")
    
    # Auto-scroll to bottom
    chat_box.see(tk.END)

# GUI window
window = tk.Tk()
window.title("Jarvis AI Assistant")
window.geometry("500x600")
window.configure(bg="#2c3e50")

# Header label
header = tk.Label(window, text="Jarvis AI", bg="#2c3e50", fg="#ecf0f1", 
                  font=("Helvetica", 18, "bold"))
header.pack(pady=10)

# Chat display area
chat_box = scrolledtext.ScrolledText(window, bg="#34495e", fg="#ecf0f1", 
                                     font=("Arial", 12), wrap=tk.WORD)
chat_box.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)
chat_box.config(state=tk.NORMAL)

# Input frame
input_frame = tk.Frame(window, bg="#2c3e50")
input_frame.pack(fill=tk.X, padx=15, pady=10)

entry = tk.Entry(input_frame, font=("Arial", 14), bg="#ecf0f1", fg="#2c3e50")
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
entry.bind("<Return>", send_message)

send_button = tk.Button(input_frame, text="Send", command=send_message, 
                        bg="#27ae60", fg="white", font=("Arial", 12, "bold"),
                        padx=20, pady=5)
send_button.pack(side=tk.RIGHT)

# Welcome message
chat_box.insert(tk.END, "Jarvis: Hello! I am your AI assistant. How can I help you today?\n\n")

window.mainloop()

