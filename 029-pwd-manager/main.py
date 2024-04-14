import json
import string
from tkinter import *
from tkinter import messagebox
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

    new_data = {
        website: {
            'email': username,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="You left something empty")

    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            username_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def search_websites():
    search_text = website_input.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError as error:
        print(error)
    else:
        for key in data:
            if key == search_text:
                login = data[key]
                username_input.delete(0, END)
                password_input.delete(0, END)
                username_input.insert(0, login['email'])
                password_input.insert(0, login['password'])


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
website_input.grid(row=1, column=1)
website_input.focus()
website_search = Button(text="Search", width=15)
website_search.grid(row=1, column=3)
website_search.config(command=search_websites)

# Email/Username
username_label = Label(text='Email/Username')
username_label.grid(row=2, column=0)
username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2)

# Password
password_label = Label(text='Password')
password_label.grid(row=3, column=0)
password_input = Entry(width=35)
password_input.grid(row=3, column=1)
generate_password = Button(text='Generate Password', width=15)
generate_password.grid(row=3, column=3)
generate_password.config(command=create_password)

# Add Button
add_button = Button(text='Add', width=21)
add_button.grid(row=4, column=1, columnspan=2)
add_button.config(command=save_password)

window.mainloop()