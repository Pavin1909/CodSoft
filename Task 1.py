import tkinter as tk
from tkinter import messagebox
import json
import os

TASKS_FILE = 'tasks.json'


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks():
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)


def update_listbox():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        title = task['title']
        status = "✔" if task['completed'] else "✘"
        listbox.insert(tk.END, f"{i+1}. [{status}] {title}")

def add_task():
    title = entry.get().strip()
    if title == "":
        messagebox.showwarning("Warning", "Task cannot be empty.")
        return
    tasks.append({"title": title, "completed": False})
    entry.delete(0, tk.END)
    update_listbox()
    save_tasks()

def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_completed():
    try:
        index = listbox.curselection()[0]
        tasks[index]['completed'] = True
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark completed.")


tasks = load_tasks()

root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("700x500") 

FONT_LARGE = ("Helvetica", 14)
FONT_MEDIUM = ("Helvetica", 12)

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

entry = tk.Entry(frame, width=50, font=FONT_LARGE)
entry.pack(side=tk.LEFT, padx=(0, 10))

add_btn = tk.Button(frame, text="Add Task", font=FONT_MEDIUM, width=12, command=add_task)
add_btn.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=80, height=15, font=FONT_LARGE, selectbackground="skyblue")
listbox.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

complete_btn = tk.Button(btn_frame, text="✔ Mark Completed", font=FONT_MEDIUM, width=18, command=mark_completed)
complete_btn.pack(side=tk.LEFT, padx=10)

delete_btn = tk.Button(btn_frame, text="🗑 Delete Task", font=FONT_MEDIUM, width=15, command=delete_task)
delete_btn.pack(side=tk.LEFT, padx=10)

update_listbox()
root.mainloop()