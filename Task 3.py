import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Too Short", "Password length must be at least 4.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_var.set(password)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for length.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.config(bg="#ccffcc")  

password_var = tk.StringVar()

tk.Label(root, text="Enter Password Length:", bg="#ccffcc", font=("Arial", 14)).pack(pady=10)
length_entry = tk.Entry(root, font=("Arial", 14), justify='center')
length_entry.pack(pady=5)

tk.Button(root, text="Generate Password", font=("Arial", 14), command=generate_password).pack(pady=10)

tk.Label(root, text="Generated Password:", bg="#ccffcc", font=("Arial", 14)).pack()
tk.Entry(root, textvariable=password_var, font=("Arial", 14), justify='center', bd=2).pack(pady=5)

root.mainloop()
