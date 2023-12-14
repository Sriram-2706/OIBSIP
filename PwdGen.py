import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    length = int(length_entry.get())

    if length < 6:
        messagebox.showwarning("Warning", "Password length should be at least 6 characters.")
        return

    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_digits = digits_var.get()
    include_symbols = symbols_var.get()

    characters = ''

    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Warning", "Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo("Success", "Password generated and copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Frame for password options
options_frame = tk.Frame(root)
options_frame.pack(padx=20, pady=20)

# Password length
length_label = tk.Label(options_frame, text="Password Length:")
length_label.grid(row=0, column=0)
length_entry = tk.Entry(options_frame)
length_entry.grid(row=0, column=1)
length_entry.insert(0, "12")

# Checkboxes for character types
uppercase_var = tk.IntVar()
lowercase_var = tk.IntVar()
digits_var = tk.IntVar()
symbols_var = tk.IntVar()

uppercase_check = tk.Checkbutton(options_frame, text="Include Uppercase", variable=uppercase_var)
lowercase_check = tk.Checkbutton(options_frame, text="Include Lowercase", variable=lowercase_var)
digits_check = tk.Checkbutton(options_frame, text="Include Digits", variable=digits_var)
symbols_check = tk.Checkbutton(options_frame, text="Include Symbols", variable=symbols_var)

uppercase_check.grid(row=1, column=0, sticky="w")
lowercase_check.grid(row=2, column=0, sticky="w")
digits_check.grid(row=3, column=0, sticky="w")
symbols_check.grid(row=4, column=0, sticky="w")

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Display generated password
password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack()

root.mainloop()
