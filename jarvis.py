import tkinter as tk
from openai import OpenAI

# Replace with your API key
client = OpenAI(api_key="AIzaSyBbQu_VSFCQzdckDBRze1ALpbKHkLuiQfs")

def send_message():
    user_message = entry.get()

    if user_message.strip() == "":
        return

    chat_box.insert(tk.END, "You: " + user_message + "\n")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are Jarvis, a helpful AI assistant."},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response.choices[0].message.content

    chat_box.insert(tk.END, "Jarvis: " + reply + "\n\n")

    entry.delete(0, tk.END)


# GUI Window
window = tk.Tk()
window.title("Jarvis Chatbot")
window.geometry("500x600")

chat_box = tk.Text(window, wrap=tk.WORD)
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(window)
entry.pack(fill=tk.X, padx=10, pady=5)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=5)

window.mainloop()