import requests
from tkinter import *
from tkinter import ttk

class RealTimeCurrencyConverter():
    def __init__(self, url):
            self.data = requests.get(url).json()
            self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

        # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount

class App(Tk):

    def __init__(self, converter):
        Tk.__init__(self)
        self.title ('Currency Converter')
        self.currency_converter = converter

        self.geometry("400x280")

        Label(self,width="300", text="Please enter details below", bg="orange",fg="white").pack()
        # Label
        self.intro_label = Label(self, text="Choose your Currency", fg='black', font=("Helvetica", 16)).place(x=100,y=20)


        self.date_label = Label(self, text = f"1 Indian Rupee equals = {self.currency_converter.convert('ZAR','USD',1)} USD \n Date : {self.currency_converter.data['date']}", relief = GROOVE, borderwidth = 2)



        # Entry box
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        self.amount_field = Entry(self, bd = 3, relief = RIDGE, justify = CENTER, validate='key', validatecommand=valid)
        self.converted_amount_field_label = Label(self, text = '', fg = 'black', bg = 'white', relief = RIDGE, justify = CENTER, width = 18, borderwidth = 3)

        # dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("ZAR") # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD") # default value

        font = ("Manrope", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable, values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 15, justify = CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable, values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 13, justify = CENTER)

        # placing
        self.from_currency_dropdown.place(x = 110, y= 50)
        self.amount_field.place(x = 110, y = 80)
        self.to_currency_dropdown.place(x = 120, y= 170)
        self.converted_amount_field_label.place(x = 120, y = 200)

        # Convert button
        self.convert_button = Button(self, text = "Convert", fg = "black", command = self.perform)
        self.convert_button.config( width=10, height=1, bg="orange")
        self.convert_button.place(x = 150, y = 115)

    def perform(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(from_curr,to_curr,amount)
        converted_amount = round(converted_amount, 2)

        self.converted_amount_field_label.config(text = str(converted_amount))

    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return string=="" or (string.count('.')<=1 and result is not None)

if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)
    App(converter)
    mainloop()








