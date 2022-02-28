""""import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
import time # Модуль для остановки программы
import smtplib # Модуль для работы с почтой

# Основной класс
class Currency:
	# Ссылка на нужную страницу
	DOLLAR_RUB = f'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&ei=suscYtTVEamvrgSGwK2YBw&ved=0ahUKEwjU9sTb3KL2AhWpl4sKHQZgC3MQ4dUDCA0&uact=5&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAELADEEMyBwgAELADEENKBAhBGABKBAhGGABQAFgAYIUEaAFwAXgAgAEAiAEAkgEAmAEAyAEKwAEB&sclient=gws-wiz'
	# Заголовки для передачи вместе с URL
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

	current_converted_price = 0
	difference = 5 # Разница после которой будет отправлено сообщение на почту

	def __init__(self):
		# Установка курса валюты при создании объекта
		self.current_converted_price = float(self.get_currency_price().replace(",", "."))

	# Метод для получения курса валюты
	def get_currency_price(self):
		# Парсим всю страницу
		full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)

		# Разбираем через BeautifulSoup
		soup = BeautifulSoup(full_page.content, 'html.parser')

		# Получаем нужное для нас значение и возвращаем его
		convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
		return convert[0].text

	# Проверка изменения валюты
	def check_currency(self):
		currency = float(self.get_currency_price().replace(",", "."))
		if currency >= self.current_converted_price + self.difference:
			print("Курс сильно вырос, может пора что-то делать?")
			self.send_mail()
		elif currency <= self.current_converted_price - self.difference:
			print("Курс сильно упал, может пора что-то делать?")
			self.send_mail()

		print("Сейчас курс: 1 доллар = " + str(currency))
		self.check_currency()
# Создание объекта и вызов метода
currency = Currency()
currency.check_currency()"""



import redis

r_conn = redis.Redis(
	host='redis-14856.c12.us-east-1-4.ec2.cloud.redislabs.com',
	port='14856',
	password='Wcg26zT6ptYPHwUw0E53hOf5d83EtvwA',
	db=0)
p=5036976963
for key in r_conn.scan_iter():
	d=key.decode('UTF-8')
	f=r_conn.get(key.decode('UTF-8')).decode('UTF-8')
	print(f'Пользователь: {d}\nКонтент: {f}')
	r_conn.delete(key)
"""print(r_conn.keys())
u=r_conn.keys()
d=r_conn.get('id_5036976963').decode('UTF-8')
print(u)
print(d)"""
"""for x in u:
	print(x)
if str('jjj') in str(u):
	print("имба")
g = 0"""
"""for x in range(10):
	g=g+1
	r_conn.set(f'id{g}', g)
	d=r_conn.get(f'id{g}').decode('UTF-8')
	print(d)"""