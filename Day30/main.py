from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
#----------------------------- PASSWORD FIND ------------------------------------ #
def find_password():
    website = input_website.get()
    try:
        with open("data.json") as data_file:
            json_data = json.load(data_file)
            try:
                if json_data[website]:
                    messagebox.showinfo(title=f"Your data",message=f"Your data for {website}\n"
                                                                   f"Email:{json_data[website]["email"]}\n"
                                                                   f"Password:{json_data[website]["password"]}")
            except KeyError:
                messagebox.showwarning(title="Warning", message="No details for the website exists")
    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="No Data File Found")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password():
    input_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    input_password.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website=input_website.get()
    email=input_user.get()
    password=input_password.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}

    if not website or not password:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as file:
                #Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", mode="w") as file:
                #Saving updated data
                json.dump(data, file, indent=4)
        finally:
            input_website.delete(0, END)
            input_user.delete(0, END)
            input_password.delete(0, END)
            input_website.focus()
            input_user.insert(END, "fulger.sorin@yahoo.com")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)
window.grid_columnconfigure(0,weight=1)
window.grid_columnconfigure(1,weight=1)
window.grid_columnconfigure(2,weight=1)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_png = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=lock_png)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=("Arial", 12, "bold"))
website_label.grid(row=1, column=0)

user_label = Label(text="Email/Username:", font=("Arial", 12, "bold"))
user_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=("Arial", 12, "bold"))
password_label.grid(row=3, column=0)

input_website = Entry(width=35)
input_website.focus()
input_website.grid(row=1, column=1)

input_user = Entry(width=35)
input_user.insert(END, "fulger.sorin@yahoo.com")
input_user.grid(row=2, column=1)

input_password = Entry(width=35)
input_password.grid(row=3, column=1)

generate_password = Button(text="Generate Password", command=generate_random_password)
generate_password.grid(row=3, column= 2)

add_button = Button(text="Add", command=add ,width=45)
add_button.grid(row=4, column=1,columnspan=2)

search_button = Button(text="Search", command=find_password, width=15)
search_button.grid(row=1, column=2)


window.mainloop()