import tkinter as tk
from tkinter import messagebox
import subprocess

def login():

    name = name_entry.get()
    roll = roll_entry.get()
    dept = dept_entry.get()

    if name == "" or roll == "" or dept == "":
        messagebox.showerror(
            "Error",
            "Please fill all fields"
        )
        return

    root.destroy()

    subprocess.Popen(
    [
        "py",
        "-3.12",
        "main.py",
        name,
        roll,
        dept
    ]
)

root = tk.Tk()

root.title("Campus Jarvis Login")
root.geometry("400x300")
root.configure(bg="#1e1e1e")

title = tk.Label(
    root,
    text="Campus Jarvis Login",
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 16, "bold")
)

title.pack(pady=15)

tk.Label(
    root,
    text="Name",
    bg="#1e1e1e",
    fg="white"
).pack()

name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

tk.Label(
    root,
    text="Roll Number",
    bg="#1e1e1e",
    fg="white"
).pack()

roll_entry = tk.Entry(root, width=30)
roll_entry.pack(pady=5)

tk.Label(
    root,
    text="Department",
    bg="#1e1e1e",
    fg="white"
).pack()

dept_entry = tk.Entry(root, width=30)
dept_entry.pack(pady=5)

login_button = tk.Button(
    root,
    text="Login",
    command=login
)

login_button.pack(pady=20)

root.mainloop()