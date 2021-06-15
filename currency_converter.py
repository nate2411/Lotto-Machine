from tkinter import *
from tkinter.ttk import Combobox
window = Tk()
window.title("Currency Converter")
window.geometry("400x280")
Label(window,width="300", text="Please enter details below", bg="orange",fg="white").pack()
Label(window, text="Choose your Currency", fg='black', font=("Helvetica", 16)).place(x=100,y=20)
currencychoosen = Combobox(window, width= 27)
currencychoosen.place(x=90, y=50)
Entry(window, width=13 ).place(x=150,y=70)
Label(window, text="Converted Too", fg='black', font=("Helvetica", 16)).place(x=130,y=110)
currencychoosen = Combobox(window, width= 27)
currencychoosen.place(x=90, y=140)
Entry(window, width=13 ).place(x=150,y=160)
Button(window, text="Convert", width=10, height=1, bg="orange", ).place(x=90, y=190)
Button(window, text="Clear", width=10, height=1, bg="orange", ).place(x=210, y=190)
Label(window, text="Amount", fg='black', font=("Helvetica", 16)).place(x=170,y=230)
Entry(window, width=13 ).place(x=150,y=250)







window.mainloop()
