#   NATHAN DE JAGER
from datetime import date
from tkinter import *
from tkinter import messagebox
import rsaidnumber
from datetime import date
from dateutil.relativedelta import relativedelta
window = Tk()


LIMIT_AGE = 18


def clear():
  id_entry.delete(0, END)



def ask_for_id():
    try:
# Calculates the age.
        id_number = rsaidnumber.parse(id_entry.get())
        birth_date = id_number.date_of_birth
        real_age = relativedelta(date.today(), birth_date.date())
        real_age = real_age.years
        # Checks if the id_number is valid.
        if len(id_entry.get()) != 13:
             messagebox.showerror("Error", "Please enter correct ID number")

        elif id_number == " ":
            messagebox.showerror("Error", "Enter correct details")

        elif real_age >= 18:
             real_age = str(real_age)
             with open("login.txt", "w+") as file:
                 file.write("id number: " + str(id_number))
             messagebox.showinfo("You are " + real_age + " years old", "You are Welcome To Play")
             window.destroy()
             import login

        else:
            if real_age < 18:
             real_age = str(real_age)
             messagebox.showinfo("You are " + real_age + " years old", "You not old Enough")
             window.destroy()

    except:
        messagebox.showinfo("NOPE TRY AGAIN!!!!", 'Please insert your ID number.')







window.title('Age Checker')
window.geometry("400x280")
Label(window, width="300", text="Please enter details below", bg="orange", fg="white").pack()
lbl = Label(window, text="Enter Your ID", fg='black', font=("Helvetica", 16)).place(x=110, y=90)
id_entry = Entry(window)
id_entry.place(x=100, y=120)
Button(window, text="Enter", width=10, height=1, bg="orange", command=ask_for_id).place(x=200, y=150)
Button(window, text="Clear", width=10, height=1, bg="orange", command=clear).place(x=70, y=150)


# if __name__ == '__main__':
#     year_of_birth = ask_for_birth_year()
#     current_year = date.today().year
#     age = current_year - year_of_birth
#     print_message(age)


window.mainloop()
