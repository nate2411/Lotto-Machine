from tkinter import *
from tkinter.ttk import Combobox
window = Tk()
variable1 = StringVar(window)
variable2 = StringVar(window)

# initialise the variables
variable1.set("currency")
variable2.set("currency")


# Function to perform real time conversion
# from one currency to another currency
def RealTimeCurrencyConversion():

    # importing required libraries
    import requests, json

    # currency code
    from_currency = variable1.get()
    to_currency = variable2.get()

    # enter your api key here
    api_key = "0f70dce1093d681579c27287"

    # base_url variable store base url
    base_url = r"https://v6.exchangerate-api.com/v6/21d57e3e0d14d58eee61f22c/latest/USD = CURRENCY_EXCHANGE_RATE"

    # main_url variable store complete url
    main_url = base_url + "&from_currency =" + from_currency + "&to_currency =" + to_currency + "&apikey =" + api_key


    # get method of requests module
    # return response object
    req_ob = requests.get(main_url)
    data = req_ob.json()
    rates = data["conversion_rates"]
    print(rates)

    # json method return json format
    # data into python dictionary data type.

    # result contains list of nested dictionaries
    result = req_ob.json()

    # parsing the required information
    Exchange_Rate = float(result["Realtime Currency Exchange Rate"]
                                              ['5. Exchange Rate'])

    # get method of Entry widget
    # returns current text  as a
    # string from text entry box.
    amount = float(cc.get())

    # calculation for the conversion
    new_amount = round(amount * Exchange_Rate, 3)

    # insert method inserting the
    # value in the text entry box.
    cc2.insert(0, str(new_amount))


# Function for clearing the Entry field
def clear_all() :
    cc.delete(0, END)
    cc2.delete(0, END)


# Driver code
if __name__ == "__main__" :


 window.title("Currency Converter")
window.geometry("400x280")
Label(window,width="300", text="Please enter details below", bg="orange",fg="white").pack()
Label(window, text="Choose your Currency", fg='black', font=("Helvetica", 16)).place(x=100,y=20)
currencychoosen = Combobox(window, width= 27)
currencychoosen.place(x=90, y=50)
cc= Entry(window, width=13 ).place(x=150,y=70)
Label(window, text="Converted Too", fg='black', font=("Helvetica", 16)).place(x=130,y=110)
currencychoosen = Combobox(window, width= 27)
currencychoosen.place(x=90, y=140)
cc2 =Entry(window, width=13 ).place(x=150,y=160)
Button(window, text="Convert", width=10, height=1, bg="orange", ).place(x=90, y=190)
Button(window, text="Clear", width=10, height=1, bg="orange", ).place(x=210, y=190)
Label(window, text="Amount", fg='black', font=("Helvetica", 16)).place(x=170,y=230)
Entry(window, width=13 ).place(x=150,y=250)







window.mainloop()
