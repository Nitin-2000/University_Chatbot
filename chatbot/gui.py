# import aiml
# import tkinter as tk
# from tkinter import scrolledtext
# import webbrowser;

# # Load AIML Kernel
# kernel = aiml.Kernel()
# kernel.learn("D:/aiip1/botdata/standard/*.aiml")  # Ensure this path is correct

# # Function to get chatbot response
# def chatbot_response(user_input):
#     return kernel.respond(user_input)

# # Function to send message and get response
# def send_message():
#     user_input = user_entry.get()
#     if user_input.strip() == "":
#         return

#     chat_area.insert(tk.END, "You: " + user_input + "\n")
#     response = chatbot_response(user_input)
#     chat_area.insert(tk.END, "Bot: " + response + "\n\n")

#     user_entry.delete(0, tk.END)  # Clear input field
#     chat_area.yview(tk.END)  # Auto-scroll to latest message

# def open_link(event):
#     webbrowser.open("https://mu.ac.in")

# # Create main window
# root = tk.Tk()
# root.title("AIML Chatbot")

# # Chat display area
# chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Arial", 12))
# chat_area.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

# # Input field
# user_entry = tk.Entry(root, width=40, font=("Arial", 12))
# user_entry.grid(column=0, row=1, padx=10, pady=5)

# # Send button
# send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12), bg="lightblue")
# send_button.grid(column=1, row=1, padx=10, pady=5)

# # Run the Tkinter event loop
# root.mainloop()

import aiml
import tkinter as tk
from tkinter import scrolledtext
import webbrowser  # To open links

# Load AIML Kernel
kernel = aiml.Kernel()
kernel.learn("D:/aiip1/botdata/standard/basic_chat.aiml")  # Ensure this path is correct

# Function to get chatbot response
def chatbot_response(user_input):
    return kernel.respond(user_input)

# Function to send message and get response
def send_message():
    user_input = user_entry.get()
    if user_input.strip() == "":
        return

    chat_area.insert(tk.END, "You: " + user_input + "\n")

    response = chatbot_response(user_input)
    
    # Check if response contains a URL and make it clickable
    if "https://" in response or "http://" in response:
        chat_area.insert(tk.END, "Bot: ", "bot")
        chat_area.insert(tk.END, response + "\n\n", "link")
    else:
        chat_area.insert(tk.END, "Bot: " + response + "\n\n")

    user_entry.delete(0, tk.END)  # Clear input field
    chat_area.yview(tk.END)  # Auto-scroll to latest message

# Function to open the Mumbai University link
def open_link(event):
    webbrowser.open("https://mu.ac.in")

# Create main window
root = tk.Tk()
root.title("AIML Chatbot")

# Chat display area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Arial", 12))
chat_area.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

# Add link styling
chat_area.tag_config("link", foreground="blue", underline=True)
chat_area.tag_bind("link", "<Button-1>", open_link)

# Input field
user_entry = tk.Entry(root, width=40, font=("Arial", 12))
user_entry.grid(column=0, row=1, padx=10, pady=5)

# Send button
send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12), bg="lightblue")
send_button.grid(column=1, row=1, padx=10, pady=5)

# Run the Tkinter event loop
root.mainloop()
