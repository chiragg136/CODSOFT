import tkinter as tk
from tkinter import messagebox

# Sample contact list
contacts = []

# Function to add a new contact
def add_contact():
    name = name_var.get()
    phone = phone_var.get()
    if name and phone:
        contacts.append({'name': name, 'phone': phone})
        update_contact_list()
        name_var.set("")
        phone_var.set("")
    else:
        messagebox.showwarning("Input Error", "Please enter both name and phone number.")

# Function to update the contact list display
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to delete a selected contact
def delete_contact():
    selected_contact = contact_listbox.curselection()
    if selected_contact:
        contacts.pop(selected_contact[0])
        update_contact_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")

# Function to edit a selected contact
def edit_contact():
    selected_contact = contact_listbox.curselection()
    if selected_contact:
        contact = contacts[selected_contact[0]]
        name_var.set(contact['name'])
        phone_var.set(contact['phone'])
        delete_contact()
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to edit.")

# Function to search for a contact
def search_contact():
    search_name = search_var.get().lower()
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        if search_name in contact['name'].lower():
            contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")
    if not contact_listbox.size():
        contact_listbox.insert(tk.END, "No contacts found.")

# Function to view all contacts
def view_all_contacts():
    view_window = tk.Toplevel(root)
    view_window.title("All Contacts")
    view_window.geometry("300x400")

    view_listbox = tk.Listbox(view_window, font=("Helvetica", 12))
    view_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

    for contact in contacts:
        view_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Initialize the main window
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x500")

# Create and place widgets
tk.Label(root, text="Contact Book", font=("Helvetica", 16)).pack(pady=10)

tk.Label(root, text="Name:", font=("Helvetica", 12)).pack(pady=5)
name_var = tk.StringVar()
name_entry = tk.Entry(root, textvariable=name_var, font=("Helvetica", 12))
name_entry.pack(pady=5)

tk.Label(root, text="Phone:", font=("Helvetica", 12)).pack(pady=5)
phone_var = tk.StringVar()
phone_entry = tk.Entry(root, textvariable=phone_var, font=("Helvetica", 12))
phone_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Contact", command=add_contact, font=("Helvetica", 12))
add_button.pack(pady=10)

edit_button = tk.Button(root, text="Edit Contact", command=edit_contact, font=("Helvetica", 12))
edit_button.pack(pady=10)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact, font=("Helvetica", 12))
delete_button.pack(pady=10)

tk.Label(root, text="Search by Name:", font=("Helvetica", 12)).pack(pady=5)
search_var = tk.StringVar()
search_entry = tk.Entry(root, textvariable=search_var, font=("Helvetica", 12))
search_entry.pack(pady=5)

search_button = tk.Button(root, text="Search", command=search_contact, font=("Helvetica", 12))
search_button.pack(pady=10)

view_button = tk.Button(root, text="View All Contacts", command=view_all_contacts, font=("Helvetica", 12))
view_button.pack(pady=10)

contact_listbox = tk.Listbox(root, font=("Helvetica", 12))
contact_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

# Start the main event loop
root.mainloop()
