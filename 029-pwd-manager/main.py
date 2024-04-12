import string
from tkinter import *
from tkinter import messagebox
import csv
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def create_password():
    length = random.randint(12, 18)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    pyperclip.copy(password)
    messagebox.showinfo(message='Password was copied to clipboard!')

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    is_ok = messagebox.askokcancel(title=website, message="Are you sure you want to save?")

    if is_ok:
        # Use 'a' for append mode, which adds to the end of the file without truncating it
        with open('passwords.csv', mode='a', newline='') as pw_file:
            # Create a writer object that will handle CSV formatting
            writer = csv.writer(pw_file)
            # Write a new row to the CSV file
            writer.writerow([website, username, password])

    website_input.delete(0, END)
    username_input.delete(0, END)
    username_input.insert(0, 'brooks@salesslider.com')
    password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


# Window
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(height=200, width=200)
canvas_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=canvas_image)
canvas.grid(row=0, column=1)

# Website
website_label = Label(text='Website')
website_label.grid(row=1, column=0)
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

# Email/Username
username_label = Label(text='Email/Username')
username_label.grid(row=2, column=0)
username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, 'brooks@salesslider.com')

# Password
password_label = Label(text='Password')
password_label.grid(row=3, column=0)
password_input = Entry(width=35)
password_input.grid(row=3, column=1)
generate_password = Button(text='Generate Password')
generate_password.grid(row=3, column=3)
generate_password.config(command=create_password)

# Add Button
add_button = Button(text='Add', width=21)
add_button.grid(row=4, column=1, columnspan=2)
add_button.config(command=save_password)

window.mainloop()
