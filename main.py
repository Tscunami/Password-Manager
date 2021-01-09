from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip            # For instantly copy text to clipboard
import os                   # For checking if file not empty
from sys import platform    # To detect which OS user using
import json                 # For saving data

GRAY = "#394867"
WHITE = "#f1f6f9"
YELLOW = "#fff8cd"
FONT_NAME = ("Courier", 12, "bold")


def get_email():
    if os.stat("email.txt").st_size != 0:
        with open("email.txt") as file:
            email = file.read()
        return email
    else:
        return ""


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
               'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            # Save email for later use
            if checked_state.get() == 1:
                with open("email.txt", mode="w") as file:
                    file.write(email)
            else:
                email_entry.delete(0, END)
                email_entry.insert(0, get_email)
            website_entry.delete(0, END)
            password_entry.delete(0, END)

    website_entry.focus()


def find_password():
    website = website_entry.get().title()

    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title=website, message=f"No Data File Found.")
    else:
        if website in data:
            print(data[website])
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\n"
                                                       f"Password: {data[website]['password']}")
        else:
            messagebox.showinfo(title=website, message=f"No details for the website exists.")


def show_data():
    from os import startfile
    startfile("data.json")


app = Tk()
app.title("🔒🔑 Password Manager 🔑🔒")
app.config(padx=50, pady=45, bg=GRAY)


canvas = Canvas(width=200, height=200, bg=GRAY, highlightthickness=0)
lock_image = PhotoImage(file="images/lock.png")

canvas.create_image(100, 80, image=lock_image)
canvas.grid(row=0, column=1)

# Defining all GUI elements
website_label = Label(text="Website:", bg=GRAY, fg="white", font=FONT_NAME)
search_button = Button(text="Search", width=15, bg=YELLOW, command=find_password)
email_label = Label(text="Email/Username:", bg=GRAY, fg="white", font=FONT_NAME)
password_label = Label(text="Password:", bg=GRAY, fg="white", font=FONT_NAME)
website_entry = Entry(width=30, bg=WHITE)
email_entry = Entry(width=45)
checked_state = IntVar()
checkbutton = Checkbutton(text="Save", variable=checked_state, bg=GRAY, font=FONT_NAME, fg="white", selectcolor=GRAY)
password_entry = Entry(width=30)
generate_button = Button(text="Generate password", command=generate_password,
                         bg=YELLOW, width=15)
add_button = Button(text="Add", width=25, command=save, bg=YELLOW, )

if platform == "win32":
    show_passwords_button = Button(text="Show Data", width=15, bg=YELLOW, command=show_data)
else:
    show_passwords_button = Button(text="Show Data", width=15, bg=YELLOW, state=DISABLED)

# Add GUI elements on the screen
website_label.grid(row=1, column=0, sticky="e")
search_button.grid(row=1, column=2, sticky="w")
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0, sticky="e")
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, get_email())
checkbutton.grid(row=2, column=2, sticky="e")
password_entry.grid(row=3, column=1, sticky="w")
generate_button.grid(row=3, column=2, sticky="w")
add_button.grid(row=4, column=1, sticky="w")
show_passwords_button.grid(row=4, column=2, sticky="w")

app.mainloop()
