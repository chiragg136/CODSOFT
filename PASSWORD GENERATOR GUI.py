import tkinter as tk
import random
import string

def generate_password(length):
    # Define different types of character sets
    Lcase = string.ascii_lowercase
    Ucase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation  # includes symbols like !@#$%^&*()

    # Combine all character sets
    all = Lcase + Ucase + digits + special

    # Generate password by randomly selecting characters from all
    password = ''.join(random.choice(all) for _ in range(length))
    return password

def generate():
    try:
        length = int(length_entry.get())
        if length <= 0:
            result_label.config(text="Password length should be greater than zero.")
        else:
            password = generate_password(length)
            result_label.config(text=f"Your new password is: {password}")
    except ValueError:
        result_label.config(text="Please enter a valid number!")

# Initialize the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

# Create and place widgets
tk.Label(root, text="Password Generator", font=("Helvetica", 16)).pack(pady=10)

tk.Label(root, text="Enter password length:", font=("Helvetica", 12)).pack(pady=5)
length_entry = tk.Entry(root, font=("Helvetica", 12))
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate, font=("Helvetica", 12))
generate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

# Start the main event loop
root.mainloop()
