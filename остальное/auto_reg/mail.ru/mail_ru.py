from selenium import webdriver
import sqlite3
import time
import random
import string
from selenium.webdriver.chrome.options import Options
import requests
from requests.auth import HTTPProxyAuth
import os
import shutil
# БАЗА ДАННЫХ  #
con = sqlite3.connect('mailru.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS mailru (
	mail TEXT,
	password TEXT,
	count INTEGER
	)''')
# БАЗА ДАННЫХ /#

# ОЧИСТИ ВРЕМЕННЫХ ФАЙЛОВ  #
def delite():
	for filename in os.listdir(folder):
		file_path = os.path.join(folder, filename)
		try:
			if os.path.isfile(file_path) or os.path.islink(file_path):
				os.unlink(file_path)
			elif os.path.isdir(file_path):
				shutil.rmtree(file_path)
		except Exception as e:
			print('всё ок')
# ОЧИСТИ ВРЕМЕННЫХ ФАЙЛОВ /#

# ЗАПУСК БРАУЗЕРА  #
options = Options()
options.add_argument("--headless")
# СКРЫВАТЬ БРАУЗЕР ИЛИ НЕТ? (Да=yes, Нет=no)
# ЗАПУСК БРАУЗЕРА /#

kolvo=input("Сколько аккаунтов создать?: ")
for zxc in range(int(kolvo)):
	folder = 'C:/Users/abssd/AppData/Local/Temp'
	delite()
	folder = 'C:/Windows/Temp'
	delite()
	folder = 'C:/Windows/Prefetch'
	delite()
	scr = "no"
	if scr == "yes":
		browser = webdriver.Chrome(options=options)
		browser.get('https://account.mail.ru/signup?from=main&rf=auth.mail.ru&app_id_mytracker=')
		mail_ru = browser.window_handles[0]
	elif scr == "no":
		browser = webdriver.Chrome()
		browser.get('https://account.mail.ru/signup?from=main&rf=auth.mail.ru&app_id_mytracker=')
		mail_ru = browser.window_handles[0]
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="fname"]').send_keys("Антонио")
	browser.find_element_by_xpath('//*[@id="lname"]').send_keys("Десперато")
	browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div/form/div[5]/div[2]/div/div[1]/div/div/div/div/div[1]/span').click()
	browser.find_element_by_xpath('//*[@id="react-select-2-option-6"]').click()
	browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div/form/div[5]/div[2]/div/div[3]/div/div/div/div[1]/span').click()
	browser.find_element_by_xpath('//*[@id="react-select-3-option-4"]').click()
	browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div/form/div[5]/div[2]/div/div[5]/div/div/div/div/div[1]/span').click()
	browser.find_element_by_xpath('//*[@id="react-select-4-option-11"]/div/div').click()
	browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div/form/div[8]/div[2]/div/label[1]/div[1]').click()
	browser.find_element_by_xpath('//*[@id="aaa__input"]').send_keys(f'fdsfssdgsdg4211tfgasftfede') #{count[0]}
	browser.find_element_by_xpath('//*[@id="password"]').send_keys("k8ki0lz1Z")
	browser.find_element_by_xpath('//*[@id="repeatPassword"]').send_keys("k8ki0lz1Z")
	browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div/form/div[17]/span').click()
	browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div/form/button').click()
	browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div/form/button').click()
	time.sleep(3)
	try:
		time.sleep(3)
		g=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div/form/div[17]/div/div/div[3]/small').text
		gg=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[3]/div/div/div/form/div[3]/p').text
		print (g)
		print(gg)
		if g == "Укажите телефон":
			print("СМЕНИТЕ ВПН")
			browser.close()
		elif gg == "Регистрация без номера телефона невозможна. Вернитесь к предыдущему шагу и укажите номер телефона.":
			print("СМЕНИТЕ ВПН")
			browser.close()
	except:
		def pov():
			conec=input("Введите капчу: ")
			browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[3]/div/div/div/form/div[5]/div/div[1]/div/div/div/div/input').send_keys(conec)
			browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[3]/div/div/div/form/button[1]/span').click()
			time.sleep(3)
			try:
				gg=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[3]/div/div/div/form/div[3]/p').text
				print(gg)
				cg=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[3]/div/div/div/form/div[5]/div/div[1]/div/div[2]/small').text
				print(cg)
				if gg == "Регистрация без номера телефона невозможна. Вернитесь к предыдущему шагу и укажите номер телефона.":
					print("СМЕНИТЕ ВПН")
					browser.close()
					pov()
				elif cg == "Вы указали неправильный код с картинки":
					print("Капча не правильно введена")
					pov()
			except:
				print("Имба")
		pov()
time.sleep(5)
browser.close()



"""	else:
		cur.execute(f'SELECT count from mailru')
		cnt = cur.fetchone()
		cnt = cnt[0]+1
		print(f"Удачно!\n{cnt}")
		cur.execute(f'INSERT INTO mailru(mail, password) VALUES ("accountbyabssduo{count[0]}", "k8ki0lz1Z")')
		cur.execute(f'UPDATE mailru set count={cnt}')
		con.commit()"""

"""cur.execute(f'DELETE FROM mailru WHERE mail="None"')
con.commit()
#Записать почты и пароли в текстовый файл? (Да=yes, Нет=no)
enter = "yes"
cur.execute(f'SELECT mail from mailru')
d = cur.fetchall()
if enter == "yes":
	txt = open("mailru_pass.txt", "w+")
	for x in d:
		txt.write(f"{x[0]}@mail.ru\n")
	txt.close()
time.sleep(40)"""





# СКРИПТ РЕГИСТРАЦИИ  #
"""cur.execute(f'INSERT into mailru(count) VALUES (0)')
con.commit()
cur.execute(f'SELECT count from mailru')
count = cur.fetchone()
print(count[0])
time.sleep(1)"""
