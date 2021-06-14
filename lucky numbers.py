from tkinter import *
window = Tk()
window.title("Lucky Numbers")
window.geometry("400x280")
Label(window,width="300", text="Please enter details below", bg="orange",fg="white").pack()
Label(window, text="Choose Your Numbers", fg='black', font=("Helvetica", 16)).place(x=100,y=20)

w = Spinbox(window, from_=1, to=49, width=4).place(x=20,y=70)
w = Spinbox(window, from_=1, to=49, width=4).place(x=90,y=70)
w = Spinbox(window, from_=1, to=49, width=4).place(x=150,y=70)
w = Spinbox(window, from_=1, to=49, width=4).place(x=210,y=70)
w = Spinbox(window, from_=1, to=49, width=4).place(x=270,y=70)
w = Spinbox(window, from_=1, to=49, width=4).place(x=330,y=70)
Button(window, text="Enter", width=10, height=1, bg="orange", ).place(x=80, y=120)
Button(window, text="Clear", width=10, height=1, bg="orange", ).place(x=220, y=120)

Label(window, text="Results", fg="black", font=("Helvetica", 16)).place(x=160,y=170)
Entry(window, width=4 , border=4).place(x=20,y=200)
Entry(window, width=4 , border=4).place(x=90,y=200)
Entry(window, width=4 , border=4).place(x=150,y=200)
Entry(window, width=4 , border=4).place(x=210,y=200)
Entry(window, width=4 , border=4).place(x=270,y=200)
Entry(window, width=4 , border=4).place(x=330,y=200)
Button(window, text="Clear", width=10, height=1, bg="orange", ).place(x=150, y=240)






window.mainloop()
