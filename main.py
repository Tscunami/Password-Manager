from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import os


GRAY = "#394867"
WHITE = "#f1f6f9"
BLUE = "#fff8cd"
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

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are details entered: \n"
                                       f"Email: {email}\n"
                                       f"Password: {password}\n"
                                       f"Is it okay to save?")
        if is_ok:
            # Save login data in file
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")

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


app = Tk()
app.title("Password Manager`")
app.config(padx=50, pady=45, bg=GRAY)


canvas = Canvas(width=200, height=200, bg=GRAY, highlightthickness=0)
lock_image = PhotoImage(file="lock.png")

canvas.create_image(100, 80, image=lock_image)
canvas.grid(row=0, column=1)

# Defining all GUI elements
website_label = Label(text="Website:", bg=GRAY, fg="white", font=FONT_NAME)
email_label = Label(text="Email/Username:", bg=GRAY, fg="white", font=FONT_NAME)
password_label = Label(text="Password:", bg=GRAY, fg="white", font=FONT_NAME)
website_entry = Entry(width=52, bg=WHITE)
email_entry = Entry(width=45)
checked_state = IntVar()
checkbutton = Checkbutton(text="Save", variable=checked_state, bg=GRAY, font=FONT_NAME, fg="white", selectcolor=GRAY)
password_entry = Entry(width=30)
generate_button = Button(text="Generate password", command=generate_password, bg=BLUE, highlightthickness=0)
add_button = Button(text="Add", width=43, command=save, bg=BLUE, )

# Add GUI elements on the screen
website_label.grid(row=1, column=0, sticky="e")
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0, sticky="e")
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, get_email())
checkbutton.grid(row=2, column=2, sticky="e")
password_entry.grid(row=3, column=1, sticky="w")
generate_button.grid(row=3, column=2, sticky="w")
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

app.mainloop()
