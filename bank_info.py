import tkinter
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
window =Tk()
window.title("BANK INFORMATION")
window.geometry("400x280")


def convert():
    window.destroy()
    import CC


def clear():
 n_1.delete(0, END)
 n_2.delete(0, END)


def enter():
   try:
       list1 = ["1", "2", "3", "4", '5', "6", "7", "8", '9', "0"]
       name_ent = n_1.get()
       number_ent = n_2.get()
       if name_ent == '':
           raise ValueError
       elif name_ent in list1:
               raise ValueError
       if number_ent == '':
                raise ValueError
       else:
        int(n_2.get())
        messagebox.showinfo(message='Details have been entered correctly:)')
       if bankchoosen.get() == 'Select Bank':
        raise ValueError
       elif bankchoosen.get() == 'FNB':
        messagebox.showinfo(message='Details have been entered correctly:)')
       elif bankchoosen.get() == 'Capitec':
        messagebox.showinfo(message='Details have been entered correctly:)')
       elif bankchoosen.get() == 'Netbank':
        messagebox.showinfo(message='Details have been entered correctly:)')
       elif bankchoosen.get() == 'Standard Bank':
        messagebox.showinfo(message='Details have been entered correctly:)')
       elif bankchoosen.get() == 'Bidvest Bank':
        messagebox.showinfo(message='Details have been entered correctly:)')
       elif bankchoosen.get() == 'Ivestec':
        messagebox.showinfo(message='Details have been entered correctly:)')


   except ValueError:
        messagebox.showerror(message='Something went wrong! Please ensure that fields are entered correctly')


Label(window,width="300", text="Please enter details below", bg="orange",fg="white").pack()
Label(window, text="Choose Your Bank", fg='black', font=("Helvetica", 16)).place(x=100,y=20)

bankchoosen = Combobox(window, width=27)
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
n_1= Entry(window, width=20  )
n_1.place(x=100,y=120)


Label(window, text="Account Number", fg='black', font=("Helvetica", 16)).place(x=100,y=160)
n_2=Entry(window, width=20 )
n_2.place(x=100,y=190)

Button(window, text="Enter", width=10, height=1, bg="orange", command=enter ).place(x=260, y=230)
Button(window, text="Clear", width=10, height=1, bg="orange", command=clear).place(x=30, y=230)
convert_btn = Button(window, text="Convert", width=10, height=1, bg="orange", command=convert)
convert_btn.place(x=145, y=230)


window.mainloop()
