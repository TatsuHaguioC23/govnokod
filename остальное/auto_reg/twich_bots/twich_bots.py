import sqlite3
#################################################################################################################################
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import logging
import keyboard
import transliterate
import requests
import sqlite3
import schedule
import time
import requests
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
from selenium import webdriver

"""con = sqlite3.connect('db.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS twitch (
	mail TEXT,
	password TEXT
	)''')
cur.execute('''CREATE TABLE IF NOT EXISTS mails (
	mail TEXT,
	password TEXT
	)''')
"""

browser = webdriver.Chrome()
browser.get('https://www.twitch.tv/nikgewing')
d = input()
if d == "":
	browser.close()
























"""browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="login-username"]').send_keys('pbkhtwjtrlrqxx')
browser.find_element_by_xpath('//*[@id="password-input"]').send_keys('k8ki0lz1!')
browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/button/div/div').click()
time.sleep(120)
browser.close()"""


"""
while True:
	#mail = input("Почта: ")
	cur.execute(f'INSERT INTO twitch(mail) VALUES ("alnjldwkgqrn@midiharmonica.com")')
	cur.execute(f'INSERT INTO twitch(password) VALUES ("k8ki0lz1Z")')
	cur.execute(f'SELECT * from twitch')
	d = cur.fetchall()
	print(d)
"""
"""joinedFile = open ("mails.txt", "r")
joinedUsers = set ()
for line in joinedFile:
	joinedUsers.add(line.strip())
joinedFile.close()
for user in joinedUsers:
	print(user)
	cur = con.execute(f'SELECT mail FROM twitch WHERE mail="{user}"')
	check = cur.fetchall()
	if not str(user) in str(check):
		cur.execute(f'INSERT INTO twitch(mail, password) VALUES ("{user}", "k8ki0lz1Z")')
		cur.execute(f'SELECT * from twitch')
d = cur.fetchall()
print(d)
"""

"""browser = webdriver.Chrome()
browser.get('https://mail.tm/ru/')
al = 0
while al < 5:
	try:
		time.sleep(0.5)
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
		browser.find_element_by_xpath('//*[@id="accounts-list"]/div/div[7]/a').click()"""
"""cur.execute(f'SELECT mail,password from mails')
d = cur.fetchall()
cur.execute(f'SELECT password from mails')
b = cur.fetchall()
for (x) in (d):
	print(f"{x[0]} : {x[1]}")"""