from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json
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
    
def find_password():
  website = website_input.get()
  try:
    with open('python_tut/day29/password-manager-start/data.json') as file:
      data = json.load(file)
  except FileNotFoundError:
    messagebox.showinfo(message='No Data File Found.', title='Oops')
  else:
    try:
      password = data[website]['password']
      email = data[website]['email']
    except KeyError:
      messagebox.showinfo(message=f'No details for the {website} exists.', title='Oops')
    else:
      messagebox.showinfo(message=f'Website: {website}\nPassword: {password}\nEmail: {email}')
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
  website = website_input.get()
  email = email_username_input.get()
  password = password_input.get()
  new_data = {
    website: {
      'email': email, 
      'password': password
    }
  }
  if website.strip() == '' or password.strip() == '':
    messagebox.showinfo(title='Oops', message='Please don\'t leave any fields empty!')
    # is_ok = messagebox.askokcancel(text='test')
  else:
    try:
      with open('python_tut/day29/password-manager-start/data.json') as file:
        data = json.load(file)
    except FileNotFoundError:
      data = new_data
    else:
      data.update(new_data)
    finally:
      with open('python_tut/day29/password-manager-start/data.json', 'w') as file:
        json.dump(data, file, indent=4)
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

website_input = Entry(width=32)
website_input.grid(column=1, row=1, sticky='w')
website_input.focus()
email_username_input = Entry(width=52)
email_username_input.grid(column=1, row=2, columnspan=2, sticky='w')
email_username_input.insert(0, 'umawanbong@gmail.com')
password_input = Entry(width=32)
password_input.grid(column=1, row=3, sticky='w')

generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(column=2, row=3, sticky='w')
add_button = Button(text='Add', width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky='w')
search_button = Button(text='Search', width=14, command=find_password)
search_button.grid(column=2, row=1, sticky='w')

window.mainloop()