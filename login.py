from tkinter import *
import re
from tkinter import messagebox
login_screen = Tk()
login_screen.geometry("400x280")
login_screen.title("Login")


def clear():
    username.delete(0, END)
    password.delete(0, END)
    email.delete(0, END)
# #defining login function
def login():
    regex = "domain@gmail.com"
    try:
# Verification of the name entry.
         if username.get() == "":
            messagebox.showinfo("NAME ENTRY", "Enter Your Name Please")
        # Verification of the email entry and the email(if it is valid or not).
         elif email.get() == "":
            messagebox.showerror("EMAIL ENTRY", "Enter An Email Please")
         elif password.get() == "":
            messagebox.showerror("Password ENTRY", "Enter An Password Please")
         elif re.search(regex, email.get()):
            messagebox.showerror("EMAIL ENTRY", "Enter A Valid Email Please")
         else:
            pass
    except:
        print("error")

    with open("login.txt", "w+") as file:
         file.write("username: " + username.get())
         file.write("\n")
         file.write("email: " + email.get())

    login_screen.destroy()
    import lucky_numbers

username_var = StringVar()
password_var = StringVar()
message_var =StringVar()
#Creating layout of login form
Label(login_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
#Username Label
Label(login_screen, text="Username * ").place(x=20,y=40)
#Username textbox
username = Entry(login_screen, textvariable=username_var)
username.place(x=90,y=42)
#Password Label
Label(login_screen, text="Password * ").place(x=20,y=80)
#Password textbox
password = Entry(login_screen, textvariable=password_var ,show="*")
password.place(x=90,y=82)
 #Email Label
Label(login_screen, text="Email  ").place(x=30,y=124)
#Email textbox
email = Entry(login_screen)
email.place(x=92,y=120)

#Label for displaying login status[success/failed]
Label(login_screen, text="",textvariable=message_var).place(x=70, y=150)
#Login button
Button(login_screen, text="Login", width=10, height=1, bg="orange", command=login).place(x=190,y=190)
Button(login_screen, text="Clear", width=10, height=1, bg="orange", command=clear).place(x=40,y=190)

login_screen.mainloop()
