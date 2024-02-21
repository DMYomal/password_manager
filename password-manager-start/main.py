import tkinter
from tkinter import messagebox
import random
import pyperclip

#Day 30
import json

window = tkinter.Tk()

    # ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers) ]
    random.shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    print(f"Your password is: {password}")
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_input.get()
    email_name = email_input.get()
    password_name = password_input.get()
    new_data = {
        website_name: {
            "email": email_name,
            "password": password_name
        }
    }

    if len(website_name) ==0 or len(password_name) ==0:
        messagebox.showwarning(title="Wanning", message="Please fill all the field")

    else:
        try:
            with open("data.json", mode="r") as data_file:
                #Reading the old data
                data = json.load(data_file)
                #Updating old data with new data
                # data.update(new_data)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                #Saving updated data
                json.dump(new_data, data_file, indent =4)

        else:
            #Updating old data with new data
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent =4)
        finally:
            clear()
    # Massagebox to check the code
    # else:
    #     is_ok = messagebox.askokcancel(title = website_name, message = f"These are the details entered: \nEmail: {email_name} \npassword: {password_name}")
    #     if is_ok:
    #         with open ("data.txt", mode ="a") as file:
    #             file.write(f"{website_name}| {email_name}| {password_name}\n")
    #         clear()


def clear():
    website_input.delete(0, "end")
    email_input.delete(0,)
    password_input.delete(0, "end")

def find_password():
    website_name = website_input.get()
    try:
        with open ("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title=f"Password of {website_name}", message=f"No {website_name} data found")
    else:
        if website_name in data:
            messagebox.showinfo(title = f"Password of {website_name}",message = f"Password: {data[website_name]['password']}\n,Email: {data[website_name]['email']}")
        else:
            messagebox.showinfo(title=f"Password of {website_name}", message="No data found")

# ---------------------------- UI SETUP ------------------------------- #

window.title("Password Manager")
window.config(padx = 50, pady =50)

canvas = tkinter.Canvas(width = 200, height = 200)
logo_img = tkinter.PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(column = 1,row =0)

website_label = tkinter.Label(text = "Website:")
website_label.grid(column = 0,row=1)

username_label = tkinter.Label(text = "Email/Username:")
username_label.grid(column = 0,row=2)

password_label = tkinter.Label(text = "Password:")
password_label.grid(column = 0,row=3)

website_input = tkinter.Entry(width = 21)
website_input.grid(column = 1,row=1,columnspan=2)
website_input.focus()

email_input = tkinter.Entry(width = 36)
email_input.grid(column = 1,row=2, columnspan=2)
email_input.insert(0,"abc@gmail.com")

password_input = tkinter.Entry(width = 21)
password_input.grid(column = 1,row=3,columnspan=2)


generate_Button = tkinter.Button(text = "Generate Password", command=generate_password, width=15)
generate_Button.grid(column = 2,row=3)

add_button = tkinter.Button(text = "Add", width=36, command=save)
add_button.grid(column = 1,row=4,columnspan=3)

search_button = tkinter.Button(text = "Search", width=14, command=find_password)
search_button.grid(column = 2,row=1)

window.mainloop()