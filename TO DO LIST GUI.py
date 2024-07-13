import tkinter as tk
from tkinter import messagebox

# Sample task list
tasks = []

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append({'task': task, 'status': 'Pending'})
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to update the task list display
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, f"{task['task']} - {task['status']}")

# Function to delete a selected task
def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        tasks.pop(selected_task[0])
        update_task_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to edit a selected task
def edit_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task = tasks[selected_task[0]]
        task_entry.delete(0, tk.END)
        task_entry.insert(0, task['task'])
        delete_task()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to edit.")

# Function to mark a selected task as completed
def mark_completed():
    selected_task = task_listbox.curselection()
    if selected_task:
        tasks[selected_task[0]]['status'] = 'Completed'
        update_task_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# Initialize the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.configure(bg="light pink")

# Create and place widgets
tk.Label(root, text="To-Do List", font=("Helvetica", 16), bg="light pink").pack(pady=10)

task_entry = tk.Entry(root, font=("Helvetica", 12))
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task, font=("Helvetica", 12))
add_button.pack(pady=5)

edit_button = tk.Button(root, text="Edit Task", command=edit_task, font=("Helvetica", 12))
edit_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, font=("Helvetica", 12))
delete_button.pack(pady=5)

complete_button = tk.Button(root, text="Mark as Completed", command=mark_completed, font=("Helvetica", 12))
complete_button.pack(pady=5)

task_listbox = tk.Listbox(root, font=("Helvetica", 12))
task_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

# Start the main event loop
root.mainloop()

