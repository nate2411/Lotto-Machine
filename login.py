from tkinter import *
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
    #getting form data
    uname=username.get()
    pwd=password.get()
    em=email.get()

    #applying empty validation
    if uname=='' or pwd=='' or em=="" :
        message_var.set("fill the empty field!!!")
    elif uname=="Nathandj" and pwd=="dejager" and em=="nathan@email.com":
        message_var.set("Login success")
        login_screen.destroy()
        import lucky_numbers


    else:
        message_var.set("Wrong username, password or Email!!!")


# #defining loginform function
# def Loginform():
#     global login_screen
#     login_screen = Tk()
#     #Setting title of screen
#     login_screen.title("Login")
#     #setting height and width of screen
#     login_screen.geometry("400x280")
#     #declaring variable
#     global  message
#     global username
#     global password
#     global email
#
#     username = StringVar()
#     password = StringVar()
#     message=StringVar()
#     #Creating layout of login form
#     Label(login_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
#     #Username Label
#     Label(login_screen, text="Username * ").place(x=20,y=40)
#     #Username textbox
#     name = Entry(login_screen, textvariable=username).place(x=90,y=42)
#     #Password Label
#     Label(login_screen, text="Password * ").place(x=20,y=80)
#     #Password textbox
#     password = Entry(login_screen, textvariable=password ,show="*").place(x=90,y=82)
#      #Email Label
#     Label(login_screen, text="Email  ").place(x=30,y=124)
#     #Email textbox
#     Entry(login_screen).place(x=92,y=120)
#
#     #Label for displaying login status[success/failed]
#     Label(login_screen, text="",textvariable=message).place(x=95,y=100)
#     #Login button
#     Button(login_screen, text="Login", width=10, height=1, bg="orange",command=login).place(x=105,y=190)
#     login_screen.mainloop()
# #calling function Loginform
# Loginform()



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
