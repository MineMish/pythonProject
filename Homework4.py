# # from bs4 import BeautifulSoup
# # import requests
# # response = requests.get("https://yandex.ru/search/?text=курс+валют&clid=2416122-4&win=572&lr=24876")
# # soup = BeautifulSoup(response.text, "lxml")
# # weather = soup.find("input", {"class":"Textinput-Control"})
# # print(weather.text)
#
# from bs4 import BeautifulSoup
# import requests
#
# response = requests.get("https://yandex.ru/search/?text=курс+валют&clid=2416122-4&win=572&lr=24876")
# soup = BeautifulSoup(response.text, "lxml")
#
# currency_rate = soup.find("input", {"class":"Textinput-Control"})
#
# if currency_rate is not None:
#     print(currency_rate['value'])
# else:
#     print("Не удалось найти курс валют.")
#
#
# # pin = 1234
# # print("Добро пожаловать!")
# # ppin = int(input("Введите ваш пин-код >>> "))
# # if ppin == pin:
# #     print("Текущий курс обмена гривны на доллары США составляет 27.7.")
# #     def convert_grivna_to_usd(grivna):
# #         usd_to_grivna_rate = 27.7  # Обновите этот курс в соответствии с актуальными данными
# #         usd = grivna / usd_to_grivna_rate
# #         return usd
# #
# #     # Пример использования:
# #     grivna = int(input("Введите сумму в гривнах, которую вы хотите обменять >>> "))
# #     usd = convert_grivna_to_usd(grivna)
# #     print(f"{grivna} гривен равно {usd} долларов США.")

import requests
from tkinter import Tk, Label, Entry, Button, StringVar, mainloop


class CurrencyConverter:
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
        self.title = 'Currency Converter'
        self.currency_converter = converter

        # StringVar is a variable class
        # we create an instance of this class
        self.var = StringVar()

        # Creating label widgets
        Label(self, text = "Enter amount", font = "arial 12 bold").pack()
        Entry(self, textvariable = self.var, justify = 'center').pack(pady=5)

        # Creating more label widgets
        Label(self, text = "Converted Amount", font = "arial 12 bold").pack()
        Label(self, text = "", textvariable = self.var, relief = 'solid').pack(pady=5)

        # Creating push button
        Button(self, text = "Convert", fg = "black", command = self.perform).pack(pady=20)

    def perform(self):
        amount = float(self.var.get())
        from_curr = 'RUB'  # replace with your currency
        to_curr = 'USD'
        converter = CurrencyConverter(f'https://api.exchangerate-api.com/v4/latest/{from_curr}')
        converted_amount = converter.convert(from_curr, to_curr, amount)
        self.var.set(converted_amount)

if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = CurrencyConverter(url)
    App(converter)
    mainloop()
