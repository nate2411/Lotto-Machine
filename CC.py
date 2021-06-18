import tkinter
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import requests

def convert_money():
     get_rates = "https://v6.exchangerate-api.com/v6/21d57e3e0d14d58eee61f22c/latest/" + currencychoosen1.get()
     rates = requests.get(get_rates).json()
     rates = float(ent.get()) * rates["conversion_rates"][currencychoosen2.get()]
     messagebox.showinfo("answer", rates)


     currencychoosen2= Combobox(window,width=20, text="")
     rates = list(rates)
     currencychoosen2["values"] = rates




window = Tk()
window.title("Currency Converter")
window.geometry("400x280")
Label(window,width="300", text="Please enter details below", bg="orange",fg="white").pack()
Label(window, text="Choose your Currency", fg='black', font=("Helvetica", 16)).place(x=100,y=20)
currencychoosen1 = Combobox(window, width= 27)
currencychoosen1.place(x=90, y=50)
cc= Entry(window, width=13 )
cc.place(x=150,y=70)
Label(window, text="Converted Too", fg='black', font=("Helvetica", 16)).place(x=130,y=110)
currencychoosen2 = Combobox(window, width= 27)
currencychoosen2.place(x=90, y=140)
cc2 = Entry(window, width=13 ).place(x=150,y=160)
c_btn = Button(window, text="Convert", width=10, height=1, bg="orange", command=convert_money)
c_btn.place(x=90, y=190)
Button(window, text="Clear", width=10, height=1, bg="orange", ).place(x=210, y=190)

Label(window, text="Amount", fg='black', font=("Helvetica", 16)).place(x=170,y=230)
ent = Entry(window, width=13)
ent.place(x=150,y=250)

window.mainloop()
