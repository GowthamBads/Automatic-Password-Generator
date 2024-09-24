import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password(min_length, use_numbers=True, use_special_chars=True):
    lower = string.ascii_lowercase
    digits = string.digits if use_numbers else ''
    special = string.punctuation if use_special_chars else ''
    
    all_chars = lower + digits + special
    if not all_chars:
        raise ValueError("At least one character set must be selected.")
    
    password = ''.join(random.choice(all_chars) for _ in range(min_length))
    return password

def on_generate():
    try:
        min_length = int(length_entry.get())
        use_numbers = numbers_var.get()
        use_special_chars = special_var.get()
        
        password = generate_password(min_length, use_numbers, use_special_chars)
        result_var.set(password)
        messagebox.showinfo("Password Generated","Generation successfull!")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Set up the main application window
app = tk.Tk()
app.title("Password Generator")
app.geometry("400x300")

# Password length label and entry
tk.Label(app, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(app)
length_entry.pack(pady=5)
length_entry.insert(0, "")

# Checkbuttons for password options
numbers_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

tk.Checkbutton(app, text="Include Numbers", variable=numbers_var).pack(pady=5)
tk.Checkbutton(app, text="Include Special Characters", variable=special_var).pack(pady=5)

# Result display and generate button
result_var = tk.StringVar()
tk.Entry(app, textvariable=result_var, state='readonly', width=30).pack(pady=10)

tk.Button(app, text="Generate Password", command=on_generate).pack(pady=10)

# Run the application
app.mainloop()
