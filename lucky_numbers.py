import random
from tkinter import *

window = Tk()
window.title("Lucky Numbers")
window.geometry("400x280")


def play():
    random_numbers = []
    while len(random_numbers) < 6:
        numbers = random.randint(1, 49)
        if numbers not in random_numbers:
            random_numbers.append(numbers)

    stuff_1.insert(0, random_numbers[0])
    stuff_2.insert(0, random_numbers[1])
    stuff_3.insert(0, random_numbers[2])
    stuff_4.insert(0, random_numbers[3])
    stuff_5.insert(0, random_numbers[4])
    stuff_6.insert(0, random_numbers[5])


Label(window, width="300", text="Please enter details below", bg="orange", fg="white").pack()
Label(window, text="Choose Your Numbers", fg='black', font=("Helvetica", 16)).place(x=100, y=20)

w_1 = Spinbox(window, from_=1, to=49, width=4).place(x=20,y=70)
w_2 = Spinbox(window, from_=1, to=49, width=4).place(x=90,y=70)
w_3 = Spinbox(window, from_=1, to=49, width=4).place(x=150,y=70)
w_4 = Spinbox(window, from_=1, to=49, width=4).place(x=210,y=70)
w_5 = Spinbox(window, from_=1, to=49, width=4).place(x=270,y=70)
w_6 = Spinbox(window, from_=1, to=49, width=4).place(x=330,y=70)
btn = Button(window, text="Enter", width=10, height=1, bg="orange", command=play)
btn.place(x=80, y=120)
Button(window, text="Clear", width=10, height=1, bg="orange", ).place(x=220, y=120)

Label(window, text="Results", fg="black", font=("Helvetica", 16)).place(x=160,y=170)
stuff_1 = Entry(window, width=4 , border=4)
stuff_1.place(x=20,y=200)
stuff_2 = Entry(window, width=4 , border=4)
stuff_2.place(x=90,y=200)
stuff_3 = Entry(window, width=4 , border=4)
stuff_3.place(x=150,y=200)
stuff_4= Entry(window, width=4 , border=4)
stuff_4.place(x=210,y=200)
stuff_5= Entry(window, width=4 , border=4)
stuff_5.place(x=270,y=200)
stuff_6= Entry(window, width=4 , border=4)
stuff_6.place(x=330,y=200)
Button(window, text="Clear", width=10, height=1, bg="orange", ).place(x=150, y=240)






window.mainloop()
