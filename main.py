from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if website == "" or email == "" or password == "":
        messagebox.showerror(title="Error", message="It's a password manager, you can't leave any fields empty.")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                      f"\nPassword: {password}"
                                                      f"\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n" )
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title('Password Manager')
window.config(pady=50, padx=50)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()
email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_username_entry.insert(0, "HatlerRyan@gmail.com")
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, sticky="W")

gen_pw_button = Button(text="Generate Password", command=generate_password)
gen_pw_button.grid(column=2, row=3, sticky="E")
add_button = Button(width=36, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
