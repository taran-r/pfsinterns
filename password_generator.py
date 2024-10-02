import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, use_uppercase, use_digits, use_special_chars):
    char_set = string.ascii_lowercase  
    if use_uppercase:
        char_set += string.ascii_uppercase
    if use_digits:
        char_set += string.digits
    if use_special_chars:
        char_set += string.punctuation
    
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(entry_length.get())
        if length < 6:
            messagebox.showerror("Error", "Password length must be at least 6 characters.")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
        return

    use_uppercase = var_uppercase.get()
    use_digits = var_digits.get()
    use_special_chars = var_special_chars.get()

    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    label_result.config(text=password)

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Enter password length (minimum 6):").pack()
entry_length = tk.Entry(root)
entry_length.pack()

var_uppercase = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include uppercase letters", variable=var_uppercase).pack()

var_digits = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include digits", variable=var_digits).pack()

var_special_chars = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include special characters", variable=var_special_chars).pack()

btn_generate = tk.Button(root, text="Generate Password", command=on_generate)
btn_generate.pack()

label_result = tk.Label(root, text="", font=("Arial", 14))
label_result.pack(pady=10)

root.mainloop()
