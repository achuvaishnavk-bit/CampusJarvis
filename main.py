import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import pyttsx3
import webbrowser
from reportlab.pdfgen import canvas
import sys
import speech_recognition as sr

# -----------------------------
# Student Details
# -----------------------------
if len(sys.argv) >= 4:

    student_name = sys.argv[1]
    student_roll = sys.argv[2]
    student_dept = sys.argv[3]

else:

    student_name = "Student"
    student_roll = ""
    student_dept = ""

# -----------------------------
# Text To Speech
# -----------------------------
engine = pyttsx3.init()
def voice_input():

    recognizer = sr.Recognizer()

    try:

        with sr.Microphone() as source:

            status_label.config(text="🎤 Listening...")
            root.update()

            audio = recognizer.listen(source, timeout=5)

            text = recognizer.recognize_google(audio)

            entry.delete(0, tk.END)
            entry.insert(0, text)

            status_label.config(text="🟢 Ready")

    except Exception:

        chat_area.insert(
            tk.END,
            "🎤 Voice input unavailable.\n"
            "Install PyAudio or use Python 3.12.\n\n"
        )

        chat_area.see(tk.END)

        status_label.config(text="🟢 Ready")

        status_label.config(text="❌ Voice Error")

def speak(text):

    status_label.config(text="🔊 Speaking...")
    root.update()

    engine.say(text)
    engine.runAndWait()

    status_label.config(text="🟢 Ready")

# -----------------------------
# Jarvis Brain
# -----------------------------
def get_response(text):

    text = text.lower()

    if "hello" in text:
        return "Hello! How can I help you?"

    elif "your name" in text:
        return "I am Campus Jarvis."

    elif "time" in text:
        return f"The time is {datetime.now().strftime('%H:%M')}"

    elif "date" in text:
        return f"Today's date is {datetime.now().strftime('%d %B %Y')}"

    elif "calculate" in text:

        expression = text.replace("calculate", "")

        try:
            result = eval(expression)
            return f"The answer is {result}"

        except:
            return "Invalid expression."

    elif "youtube" in text:

        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif "google" in text:

        webbrowser.open("https://google.com")
        return "Opening Google"

    elif "ieee" in text:

        webbrowser.open("https://ieeexplore.ieee.org")
        return "Opening IEEE website"

    elif "ohm" in text:

        return "Ohm's law states that Voltage equals Current multiplied by Resistance."

    elif "kirchhoff" in text:

        return "Kirchhoff's current law states that the algebraic sum of currents entering a node is zero."

    elif "transistor" in text:

        return "A transistor is used for switching and amplification."

    elif "resistor" in text:

        return "A resistor opposes current flow."

    elif "semiconductor" in text:

        return "A semiconductor has conductivity between a conductor and an insulator."

    elif "ece subjects" in text:

        return "Mathematics, Physics, Basic Electrical Engineering, C Programming and Engineering Graphics."

    elif "bye" in text:

        return "Goodbye!"

    else:

        return "I understand your message."

# -----------------------------
# Send Message
# -----------------------------
def send_message():

    user_text = entry.get()

    if user_text.strip() == "":
        return

    chat_area.insert(
        tk.END,
        f"You: {user_text}\n"
    )

    response = get_response(user_text)

    chat_area.insert(
        tk.END,
        f"Jarvis: {response}\n\n"
    )

    chat_area.see(tk.END)

    speak(response)

    entry.delete(0, tk.END)

# -----------------------------
# Clear Chat
# -----------------------------
def clear_chat():

    chat_area.delete("1.0", tk.END)

# -----------------------------
# Save PDF
# -----------------------------
def save_pdf():

    c = canvas.Canvas("chat_log.pdf")

    c.drawString(
        50,
        820,
        f"Student Name: {student_name}"
    )

    c.drawString(
        50,
        800,
        f"Roll Number: {student_roll}"
    )

    c.drawString(
        50,
        780,
        f"Department: {student_dept}"
    )

    text = chat_area.get("1.0", tk.END)

    y = 740

    for line in text.split("\n"):

        c.drawString(50, y, line)
        y -= 20

        if y < 50:
            c.showPage()
            y = 800

    c.save()

    speak("Chat log saved as PDF")

# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()

root.title("🤖 Campus Jarvis")

root.geometry("900x650")

root.configure(bg="#1e1e1e")

# -----------------------------
# Header
# -----------------------------
title_label = tk.Label(
    root,
    text="🤖 CAMPUS JARVIS",
    bg="#1e1e1e",
    fg="cyan",
    font=("Arial", 20, "bold")
)

title_label.pack(pady=10)

status_label = tk.Label(
    root,
    text="🟢 Ready",
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 12)
)

status_label.pack()

# -----------------------------
# Chat Area
# -----------------------------
chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    bg="#252526",
    fg="white",
    insertbackground="white",
    font=("Consolas", 11)
)

chat_area.pack(
    padx=10,
    pady=10,
    fill=tk.BOTH,
    expand=True
)

# Welcome Message
chat_area.insert(
    tk.END,
    f"Welcome {student_name}\n"
)

chat_area.insert(
    tk.END,
    f"Roll Number : {student_roll}\n"
)

chat_area.insert(
    tk.END,
    f"Department  : {student_dept}\n\n"
)

chat_area.insert(
    tk.END,
    "Campus Jarvis is Ready.\n\n"
)

# -----------------------------
# Input Box
# -----------------------------
entry = tk.Entry(
    root,
    bg="#3c3c3c",
    fg="white",
    insertbackground="white",
    font=("Arial", 12)
)

entry.pack(
    fill=tk.X,
    padx=10,
    pady=5
)

entry.bind(
    "<Return>",
    lambda event: send_message()
)

# -----------------------------
# Buttons
# -----------------------------
button_frame = tk.Frame(
    root,
    bg="#1e1e1e"
)

button_frame.pack(pady=10)

send_button = tk.Button(
    button_frame,
    text="💬 Send",
    bg="#0078D7",
    fg="white",
    command=send_message
)

send_button.grid(row=0, column=0, padx=5)

save_button = tk.Button(
    button_frame,
    text="📄 Save PDF",
    bg="#0078D7",
    fg="white",
    command=save_pdf
)

save_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(
    button_frame,
    text="🗑 Clear Chat",
    bg="#0078D7",
    fg="white",
    command=clear_chat
)

voice_button = tk.Button(
    button_frame,
    text="🎤 Voice",
    bg="#0078D7",
    fg="white",
    command=voice_input
)

voice_button.grid(row=0, column=3, padx=5)
clear_button.grid(row=0, column=2, padx=5)

# -----------------------------
# Run
# -----------------------------
root.mainloop()