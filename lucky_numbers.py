import random
from tkinter import *
from tkinter import messagebox
from playsound import playsound

window = Tk()
window.title("Lucky Numbers")
window.geometry("400x280")

var = IntVar(window)
var2 = IntVar(window)
var3 = IntVar(window)
var4 = IntVar(window)
var5 = IntVar(window)
var6 = IntVar(window)


def reset():
    var.set(1)
    var2.set(1)
    var3.set(1)
    var4.set(1)
    var5.set(1)
    var6.set(1)


def clear():
    stuff_1.delete(0, END)
    stuff_2.delete(0, END)
    stuff_3.delete(0, END)
    stuff_4.delete(0, END)
    stuff_5.delete(0, END)
    stuff_6.delete(0, END)


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

    random_numbers = set(random_numbers)
    numbers_to_enter = {int(w_1.get()), int(w_2.get()), int(w_3.get()), int(w_4.get()), int(w_5.get()), int(w_6.get())}
    matched_numbers = random_numbers.intersection(numbers_to_enter)
    count = len(matched_numbers)
    print(count)
    if count == 1:
        playsound("Mario.mp3")
        messagebox.showinfo("NOT YOUR DAY (⌣́_⌣̀)", "Better luck next time. You have 1 number correct ಠ_ಠ")

    elif count == 2:
        playsound("Drumroll.mp3")
        messagebox.showinfo("YOU WON", "You have 2 numbers correct, You won a R20.00. CLAIM YOUR PRIZE ( ͡° ͜ʖ ͡°)")
        with open("login.txt", "w+") as file:
             file.write("numbers: " + str(numbers_to_enter))
             file.write("\n")
             file.write("matched numbers: " + str(matched_numbers))

        window.destroy()
        import bank_info
    elif count == 3:
        playsound("Drumroll.mp3")
        messagebox.showinfo("YOU ARE A WINNER", "You have 3 numbers correct. You won a R100.50. CLAIM YOUR PRIZE ( ͡° ͜ʖ ͡°)")
        window.destroy()
        import bank_info
    elif count == 4:
        playsound("Drumroll.mp3")
        messagebox.showinfo("YOU ARE A WINNER ", "You have 4 numbers correct. You won a R2384.00. CLAIM YOUR PRIZE ( ͡° ͜ʖ ͡°)")
        window.destroy()
        import bank_info
    elif count == 5:
        playsound("Drumroll.mp3")
        messagebox.showinfo("YOU ARE A WINNER", "You have 5 numbers correct. You won a R8584.00. CLAIM YOUR PRIZE ( ͡° ͜ʖ ͡°) ")
        window.destroy()
        import bank_info
    elif count == 6:
        playsound("Drumroll.mp3")
        messagebox.showinfo("YOU ARE A WINNER", "You have 6 numbers correct. You wom a R10000.00. CLAIM YOUR PRIZE ( ͡° ͜ʖ ͡°) ")
        window.destroy()
        import bank_info
    else:
        playsound("Mario.mp3")
        messagebox.showinfo("NOT YOUR DAY (⌣́_⌣̀)", "Better luck next time. You have 0 numbers correct ಠ_ಠ")


Label(window, width="300", text="Please enter details below", bg="orange", fg="white").pack()
Label(window, text="Choose Your Numbers", fg='black', font=("Helvetica", 16)).place(x=100, y=20)

w_1 = Spinbox(window, from_=1, to=49, width=4, textvariable=var)
w_1.place(x=20, y=70)
w_2 = Spinbox(window, from_=1, to=49, width=4, textvariable=var2)
w_2.place(x=90, y=70)
w_3 = Spinbox(window, from_=1, to=49, width=4, textvariable=var3)
w_3.place(x=150, y=70)
w_4 = Spinbox(window, from_=1, to=49, width=4, textvariable=var4)
w_4.place(x=210, y=70)
w_5 = Spinbox(window, from_=1, to=49, width=4, textvariable=var5)
w_5.place(x=270, y=70)
w_6 = Spinbox(window, from_=1, to=49, width=4, textvariable=var6)
w_6.place(x=330, y=70)
btn = Button(window, text="Enter", width=10, height=1, bg="orange", command=play)
btn.place(x=80, y=120)
Button(window, text="Reset", width=10, height=1, bg="orange", command=reset).place(x=220, y=120)

Label(window, text="Results", fg="black", font=("Helvetica", 16)).place(x=160, y=170)
stuff_1 = Entry(window, width=4, border=4)
stuff_1.place(x=20, y=200)
stuff_2 = Entry(window, width=4, border=4)
stuff_2.place(x=90, y=200)
stuff_3 = Entry(window, width=4, border=4)
stuff_3.place(x=150, y=200)
stuff_4 = Entry(window, width=4, border=4)
stuff_4.place(x=210, y=200)
stuff_5 = Entry(window, width=4, border=4)
stuff_5.place(x=270, y=200)
stuff_6 = Entry(window, width=4, border=4)
stuff_6.place(x=330, y=200)
Button(window, text="Clear", width=10, height=1, bg="orange", command=clear).place(x=150, y=240)


window.mainloop()
