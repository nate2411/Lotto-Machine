import tkinter
from tkinter import *
from tkinter.ttk import Combobox
window =Tk()
window.title("BANK INFORMATION")
window.geometry("400x280")

Label(window,width="300", text="Please enter details below", bg="orange",fg="white").pack()
Label(window, text="Choose Your Bank", fg='black', font=("Helvetica", 16)).place(x=100,y=20)

bankchoosen = Combobox(window, width= 27)
bankchoosen.place(x=80, y=50)

bankchoosen['values'] = ('Standard Bank ',
                          'Capitec',
                         'Nedbank ',
                         'Bidvest Bank',
                         'Absa',
                         'FNB',
                         'Investec'
                         )
bankchoosen.current()

Label(window, text="Account Holder Name", fg='black', font=("Helvetica", 16)).place(x=80,y=90)
Entry(window, width=20  ).place(x=100,y=120)


Label(window, text="Account Number", fg='black', font=("Helvetica", 16)).place(x=100,y=160)
Entry(window, width=20  ).place(x=100,y=190)

Button(window, text="Enter", width=10, height=1, bg="orange", ).place(x=220, y=230)
Button(window, text="Clear", width=10, height=1, bg="orange", ).place(x=60, y=230)






mainloop()
