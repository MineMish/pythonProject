# from bs4 import BeautifulSoup
# import requests
# response = requests.get("https://yandex.ru/search/?text=курс+валют&clid=2416122-4&win=572&lr=24876")
# soup = BeautifulSoup(response.text, "lxml")
# weather = soup.find("input", {"class":"Textinput-Control"})
# print(weather.text)

from bs4 import BeautifulSoup
import requests

response = requests.get("https://yandex.ru/search/?text=курс+валют&clid=2416122-4&win=572&lr=24876")
soup = BeautifulSoup(response.text, "lxml")

currency_rate = soup.find("input", {"class":"Textinput-Control"})

if currency_rate is not None:
    print(currency_rate['value'])
else:
    print("Не удалось найти курс валют.")


# pin = 1234
# print("Добро пожаловать!")
# ppin = int(input("Введите ваш пин-код >>> "))
# if ppin == pin:
#     print("Текущий курс обмена гривны на доллары США составляет 27.7.")
#     def convert_grivna_to_usd(grivna):
#         usd_to_grivna_rate = 27.7  # Обновите этот курс в соответствии с актуальными данными
#         usd = grivna / usd_to_grivna_rate
#         return usd
#
#     # Пример использования:
#     grivna = int(input("Введите сумму в гривнах, которую вы хотите обменять >>> "))
#     usd = convert_grivna_to_usd(grivna)
#     print(f"{grivna} гривен равно {usd} долларов США.")
