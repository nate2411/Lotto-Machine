#   NATHAN DE JAGER
from datetime import date
from tkinter import *
from tkinter import messagebox

window = Tk()


LIMIT_AGE = 18

def clear():
  age_entry.delete(0, END)


def ask_for_birth_year():
    try:
        # nb = int(input('Enter Year Of Birth: '))
        nb = int(age_entry.get())
        if nb < 0:
            print('Invalid year')
        else:
            print(nb)
            current_year = date.today().year
            age = current_year - nb
            print_message(age)

    except ValueError:
        messagebox.showinfo("NOPE TRY AGAIN!!!!",'This is not a number, try again.')
        window.destroy()

def print_message(age):
    my_text = 'You are %d years old.'
    if age < LIMIT_AGE:
        messagebox.showinfo("YOU  NOT OLD ENOUGH!" ,'Goodbye!.' + my_text % age )
        window.destroy()

    else:
        messagebox.showinfo('Welcome To The Play.', my_text % age)
        window.destroy()
        import login


window.title('Age Checker')
window.geometry("400x280")
Label(window, width="300", text="Please enter details below", bg="orange", fg="white").pack()
lbl = Label(window, text="Enter Year of Birth", fg='black', font=("Helvetica", 16)).place(x=100, y=90)
age_entry = Entry(window)
age_entry.place(x=100, y=120)
Button(window, text="Enter", width=10, height=1, bg="orange", command=ask_for_birth_year).place(x=200, y=150)
Button(window, text="Clear", width=10, height=1, bg="orange", command=clear).place(x=70, y=150)


# if __name__ == '__main__':
#     year_of_birth = ask_for_birth_year()
#     current_year = date.today().year
#     age = current_year - year_of_birth
#     print_message(age)


window.mainloop()
