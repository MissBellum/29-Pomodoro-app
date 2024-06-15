from tkinter import *
from tkinter import messagebox
import json
from random import choice, randint, shuffle

# import pyperclip to copy string to clipboard

FONT = ("Cambria", 10, "normal")


# ---------------------------- SEARCH FILE -------------------------------------- #
def search():
    website = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError as e:
        print(f"{e}")
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
            email_entry.delete(0, END)
            email_entry.insert(0, f"{email}")
            p_word_entry.insert(0, f"{password}")
        else:
            messagebox.showinfo(f"No details for {website} found")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")

    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = pass_letters + pass_numbers + pass_symbols
    shuffle(password_list)

    password = "".join(password_list)
    p_word_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_file():
    website = web_entry.get()
    email = email_entry.get()
    password = p_word_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) < 2 or len(email) < 11 or len(password) < 8:
        messagebox.showinfo(title="Oops", message="Please make sure all entries are filled")
    else:
        try:
            with open("data.json", "r") as data_store:
                data = json.load(data_store)

        except FileNotFoundError:
            with open("data.json", "w") as data_store:
                json.dump(new_data, data_store, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_store:
                json.dump(data, data_store, indent=4)

        finally:
            web_entry.delete(0, END)
            p_word_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvage = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=canvage)
canvas.grid(row=0, column=1)

# Labels
web_label = Label(text="Website:", font=FONT)
web_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", font=FONT)
email_label.grid(row=2, column=0)

p_word_label = Label(text="Password:", font=FONT)
p_word_label.grid(row=3, column=0)

# Entries
web_entry = Entry(width=25, highlightthickness=0)
web_entry.grid(row=1, column=1)
web_entry.focus()

email_entry = Entry(width=40)
email_entry.insert(END, "anjaiqwoonz@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

p_word_entry = Entry(width=25, highlightthickness=0)
p_word_entry.grid(row=3, column=1)

generate_p_word = Button(text="Generate Password", width=16, font=FONT, highlightthickness=0, command=generate)
generate_p_word.grid(row=3, column=2)

save_p_word = Button(text="Add", width=40, highlightthickness=0, command=save_file)
save_p_word.grid(row=4, column=1, columnspan=2)

search = Button(text="Search", highlightthickness=0, width=14, command=search)
search.grid(row=1, column=2)

window.mainloop()
