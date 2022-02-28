from selenium import webdriver
import sqlite3
import time
import random
import string
import shutil
import os
from selenium.webdriver.chrome.options import Options
"""# БАЗА ДАННЫХ  #
con = sqlite3.connect('mails.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS mails (
	mail TEXT,
	password TEXT
	)''')
# БАЗА ДАННЫХ /#


# ЗАПУСК БРАУЗЕРА  #
options = Options()
options.add_argument("--headless")
# СКРЫВАТЬ БРАУЗЕР ИЛИ НЕТ? (Да=yes, Нет=no)
scr = "yes"
if scr == "yes":
	browser = webdriver.Chrome(options=options)
	browser.get('https://mail.tm/ru/')
if scr == "no":
	browser = webdriver.Chrome()
	browser.get('https://mail.tm/ru/')
	mail_tm = browser.window_handles[0]
# ЗАПУСК БРАУЗЕРА /#

#Очистить таблицу от почт и паролей и удалить текстовый файл? (Да=yes, Нет=no)
clear = "no"
if clear == "yes":
	cur.execute(f'DELETE from mails')
	con.commit()
	open('mail_pass.txt', 'w').close()

# СКРИПТ РЕГИСТРАЦИИ  #
al = 0
while al < 666: #Здесь ставим число аккаунтов
	try:
		time.sleep(0.8)
		browser.find_element_by_xpath('//*[@id="accounts-menu"]').click()
		time.sleep(0.1)
		mail = browser.find_element_by_xpath('//*[@id="accounts-list"]/div/div[1]/p[2]').text
		passw = browser.find_element_by_xpath('//*[@id="accounts-list"]/div/div[1]/p[3]/span').text
		browser.find_element_by_xpath('//*[@id="accounts-list"]/div/div[7]/a').click()
		if mail == "":
			print("не получил почту")
		else:
			cur.execute(f'INSERT INTO mails(mail, password) VALUES ("{mail}", "{passw}")')
			con.commit()
			print('Удачно!')
			al=al+1
			print(al)
	except:
		print('Ошибка!')
		browser.find_element_by_xpath('//*[@id="accounts-list"]/div/div[7]/a').click()

#Записать почты и пароли в текстовый файл? (Да=yes, Нет=no)
enter = "yes"
cur.execute(f'SELECT mail,password from mails')
d = cur.fetchall()
if enter == "yes":
	txt = open("mail_pass.txt", "w+")
	for x in d:
		txt.write(f"{x[0]}:{x[1]}\n")
	txt.close()

browser.close()"""