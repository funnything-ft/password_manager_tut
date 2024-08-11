from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
  website = website_input.get()
  email = email_username_input.get()
  password = password_input.get()
  if website.strip() == '' or password.strip() == '':
    messagebox.showinfo(title='Oops', message='Please don\'t leave any fields empty!')
    return
  is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email}\nPassword: {password}\n Is it ok to save?')
  if is_ok:
    with open('python_tut/day29/password-manager-start/data.txt', 'a') as file:
      file.write(f'{website} | {email} | {password}\n')
    website_input.delete(0, END)
    password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='python_tut/day29/password-manager-start/logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
email_username_label = Label(text='Email/Username:')
email_username_label.grid(column=0, row=2)
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

website_input = Entry(width=50)
website_input.grid(column=1, row=1, columnspan=2, sticky='w')
website_input.focus()
email_username_input = Entry(width=50)
email_username_input.grid(column=1, row=2, columnspan=2, sticky='w')
email_username_input.insert(0, 'umawanbong@gmail.com')
password_input = Entry(width=32)
password_input.grid(column=1, row=3, sticky='w')

generate_password_button = Button(text='Generate Password', padx=0, command=generate_password)
generate_password_button.grid(column=2, row=3, sticky='w')
add_button = Button(text='Add', width=42, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky='w')

window.mainloop()