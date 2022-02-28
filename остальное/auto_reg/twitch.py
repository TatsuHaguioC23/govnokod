from selenium import webdriver
import sqlite3
import time
import random
import string
from selenium.webdriver.chrome.options import Options
# БАЗА ДАННЫХ  #
con = sqlite3.connect('twitch.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS twitch (
	mail TEXT,
	password TEXT
	)''')
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


# ЗАПУСК БРАУЗЕРА /#

def generate_random_string(length):
	letters = string.ascii_lowercase
	rand_string = ''.join(random.choice(letters) for i in range(length))
	jk = ("Random string of length", length, "is:", rand_string)
	print(jk)

# СКРИПТ РЕГИСТРАЦИИ  #
al = 0
while al < 5: #Здесь ставим число аккаунтов
	try:
		time.sleep(0.8)
		browser.find_element_by_xpath('//*[@id="accounts-menu"]').click()
		time.sleep(0.1)
		mail = browser.find_element_by_xpath('//*[@id="accounts-list"]/div/div[1]/p[2]').text
		passw = browser.find_element_by_xpath('//*[@id="accounts-list"]/div/div[1]/p[3]/span').text
		browser.find_element_by_xpath('//*[@id="accounts-list"]/div/div[5]/a').click()
		browser.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div/div[2]/div[2]/span[1]/button').click()
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
"""# СКРИПТ РЕГИСТРАЦИИ /#
browser.switch_to.window(twitch_com)
letters = string.ascii_lowercase
lgin = ''.join(random.choice(letters) for i in range(8))
print(prsaw = ''.join(random.choice(letters) for i in range(14))
print(lgin)
print(prsaw)
print(prsaw)
cur.execute(f'SELECT mail,password from mails')
d = cur.fetchall()
for x in d:
	print(f"{x[0]} : {x[1]}")
cur.execute(f'SELECT mail from mails')
jh = cur.fetchone()
print(jh[0])
browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[2]/button').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="signup-username"]').send_keys(lgin)
browser.find_element_by_xpath('//*[@id="password-input"]').send_keys("Ogks;M-0")
browser.find_element_by_xpath('//*[@id="password-input-confirmation"]').send_keys("Ogks;M-0")
browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/div/div[2]/div[1]/div/input').send_keys("9")
browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/div/div[2]/div[2]/select/option[4]').click()
browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/div/div[2]/div[3]/div/input').send_keys("1989")
browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[4]/div/div[2]/button').click()
browser.find_element_by_xpath('//*[@id="email-input"]').send_keys("vglwfwruvmr@midiharmonica.com")
time.sleep(0.5)
browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[5]/button').click()
# В самом конце выводит все почты и пароли в формате mail : password (можете сами изменить, поменяв в самом конце)
"""

#Записать почты и пароли в текстовый файл? (Да=yes, Нет=no)
enter = "yes"
cur.execute(f'SELECT mail,password from mails')
d = cur.fetchall()
if enter == "yes":
	txt = open("tw_mp.txt", "w+")
	for x in d:
		txt.write(f"{x[0]}:{x[1]}\n")
	txt.close()

#Очистить таблицу от почт и паролей и удалить текстовый файл? (Да=yes, Нет=no)
clear = "no"
if clear == "yes":
	cur.execute(f'DELETE from mails')
	con.commit()
	open('mail_pass.txt', 'w').close()
browser.close()