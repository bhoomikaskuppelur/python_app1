
import tkinter as tk
from tkinter import messagebox
import random
import string

# -----------------------------
# Strong Password Generator
# -----------------------------

def generate_password():
    username = username_entry.get().strip()

    if not username:
        messagebox.showwarning("Input Required", "Please enter your username.")
        return

    # Keep only letters from username
    name_part = "".join(ch for ch in username if ch.isalpha())

    if len(name_part) >= 4:
        name_part = name_part[:2] + name_part[-2:]
    elif len(name_part) > 0:
        name_part = name_part
    else:
        name_part = "User"

    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    symbol = random.choice("!@#$%^&*()-_=+?")

    remaining_length = 16 - (len(name_part) + 4)

    characters = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*()-_=+?"
    )

    random_part = [random.choice(characters) for _ in range(max(remaining_length, 4))]

    password_list = list(name_part + uppercase + lowercase + digit + symbol) + random_part

    random.shuffle(password_list)

    password = "".join(password_list[:16])

    password_var.set(password)


def copy_password():
    password = password_var.get()

    if password == "":
        messagebox.showinfo("Info", "Generate a password first.")
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

    messagebox.showinfo("Copied", "Password copied to clipboard!")


# -----------------------------
# GUI
# -----------------------------

root = tk.Tk()
root.title("Strong Password Generator")
root.geometry("500x320")
root.resizable(False, False)
root.configure(bg="#f4f4f4")

title = tk.Label(
    root,
    text="Strong Password Generator",
    font=("Arial", 18, "bold"),
    bg="#f4f4f4"
)
title.pack(pady=15)

username_label = tk.Label(
    root,
    text="Enter Username",
    font=("Arial", 11),
    bg="#f4f4f4"
)
username_label.pack()

username_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 12)
)
username_entry.pack(pady=8)

generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    width=20,
    command=generate_password
)
generate_btn.pack(pady=10)

password_var = tk.StringVar()

password_entry = tk.Entry(
    root,
    textvariable=password_var,
    width=35,
    font=("Consolas", 13),
    justify="center"
)
password_entry.pack(pady=10)

copy_btn = tk.Button(
    root,
    text="Copy Password",
    font=("Arial", 11, "bold"),
    bg="#2196F3",
    fg="white",
    width=20,
    command=copy_password
)
copy_btn.pack(pady=10)

note = tk.Label(
    root,
    text="Generated password contains letters, numbers and symbols.",
    font=("Arial", 9),
    fg="gray",
    bg="#f4f4f4"
)
note.pack(pady=10)

root.mainloop()

