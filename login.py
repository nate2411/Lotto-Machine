from tkinter import *
#defining login function
def login():
    #getting form data
    uname=username.get()
    pwd=password.get()
    em=email.get()
    id=idNumber.get()
    #applying empty validation
    if uname=='' or pwd=='' or em=="" or id=="":
        message.set("fill the empty field!!!")
    else:
      if uname=="Nathandj" and pwd=="dejager" and em=="nathan@email.com" and id=="12345678":
       message.set("Login success")
      else:
       message.set("Wrong username or password!!!")
#defining loginform function
def Loginform():
    global login_screen
    login_screen = Tk()
    #Setting title of screen
    login_screen.title("Login")
    #setting height and width of screen
    login_screen.geometry("400x280")
    #declaring variable
    global  message
    global username
    global password
    global email
    global idNumber
    username = StringVar()
    password = StringVar()
    message=StringVar()
    #Creating layout of login form
    Label(login_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    #Username Label
    Label(login_screen, text="Username * ").place(x=20,y=40)
    #Username textbox
    Entry(login_screen, textvariable=username).place(x=90,y=42)
    #Password Label
    Label(login_screen, text="Password * ").place(x=20,y=80)
    #Password textbox
    Entry(login_screen, textvariable=password ,show="*").place(x=90,y=82)
     #Email Label
    Label(login_screen, text="Email  ").place(x=30,y=124)
    #Email textbox
    Entry(login_screen).place(x=92,y=120)
     # ID Label
    Label(login_screen, text="ID Number  ").place(x=9,y=170)
    #ID textbox
    Entry(login_screen).place(x=91,y=170)
    #Label for displaying login status[success/failed]
    Label(login_screen, text="",textvariable=message).place(x=95,y=100)
    #Login button
    Button(login_screen, text="Login", width=10, height=1, bg="orange",command=login).place(x=105,y=200)
    login_screen.mainloop()
#calling function Loginform
Loginform()
