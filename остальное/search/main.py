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
from config import *
from weather_code import *
#################################################################################################################################
storage = MemoryStorage()
bot = Bot(token=telegram_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s', level=logging.INFO,)
#################################################################################################################################
con = sqlite3.connect('db.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users (
	id INTEGER,
	username TEXT,
	lang TEXT DEFAULT('ru'),
	balance REAL DEFAULT(0)
	)''')
cur.execute('''CREATE TABLE IF NOT EXISTS subs (
	id INTEGER,
	wthsub TEXT DEFAULT('no'),
	wthtimee TEXT,
	wthtimezone TEXT,
	wthtown TEXT
	)''')
cur.execute('''CREATE TABLE IF NOT EXISTS spam (
	txt TEXT
	)
	''')
con.close()
#################################################################################################################################
########################################################## Клавиатуры ###########################################################
#################################################################################################################################
def keyboard_menu():
	keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
	menu = {'Погода': 'get_wth', 'Настройки': 'settings', 'Тех. поддержка☎️': 'tp'}
	for zxc in menu:
		keyboard.insert(InlineKeyboardButton(zxc, callback_data=menu[zxc]))
	return keyboard
#################################################################################################################################
def keyboard_danet():
	keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
	danet = {'Да':'yes', 'Нет': 'net'}
	for zxc in danet:
		keyboard.insert(InlineKeyboardButton(zxc, callback_data=danet[zxc]))
	return keyboard
#################################################################################################################################
def keyboard_settings(id):
	keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
	settings = {'Сервисы': 'serv', 'Язык': 'lang', 'Рассылка': 'spam'}

	for zxc in settings:
		keyboard.insert(InlineKeyboardButton(zxc, callback_data=settings[zxc]))

	if id in admins:
		services = {'Рассылка': 'spam','Выдать баланс': 'givebal', 'Забрать баланс': 'takebal'}
		keyboard.add(InlineKeyboardButton('➖➖➖➖Админ панель➖➖➖➖', callback_data='_'))
		for zxc in services:
			keyboard.insert(InlineKeyboardButton(zxc, callback_data=services[zxc]))
	return keyboard
#################################################################################################################################
def keyboard_serv():
	keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
	serv = {'Погода': 'wth'}
	for zxc in serv:
	  keyboard.insert(InlineKeyboardButton(zxc, callback_data=serv[zxc]))
	return keyboard
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
@dp.message_handler(Command("start"), state=None)
async def welcome(message):
	con = sqlite3.connect('db.db')
	cur = con.cursor()
	cur.execute('SELECT id FROM users')
	u = cur.fetchall()
	if not str(message.from_user.id) in str(u):
		await bot.send_message(5036976963, f'Новый чел\nid: {message.from_user.id} username: {message.from_user.username} ({message.from_user.first_name} {message.from_user.last_name})')
		con.execute(f'INSERT INTO users(id) VALUES ({message.from_user.id})')
		con.commit()
		con.close()
		print(message.from_user.language_code)
	start_message = f'Привет, {message.from_user.first_name} 👋.\nБот постоянно дополняется всякими штуками.\nЕсли хочешь предложить что-нибудь, то можешь написать нам.'
	await bot.send_message(message.chat.id, start_message, reply_markup=keyboard_menu())
#################################################################################################################################
@dp.message_handler(Command("test"), state=None)
async def welcome(message):
	con = sqlite3.connect('db.db')
	cur = con.cursor()
	cur.execute('SELECT * FROM users')
	y = cur.fetchall()
	cur.execute('SELECT * FROM subs')
	u = cur.fetchall()
	cur.execute('SELECT * FROM spam')
	i = cur.fetchall()
	await bot.send_message(5036976963, text=f"{y}\n{u}\n{i}")
	con.close()

def weather_ras():
	cur.execute(f'SELECT weather FROM subs WHERE id=({message.chat.id}')
#################################################################################################################################
#@dp.message_handler(Command("test"), state=None)
#async def getinf(message):

#################################################################################################################################
@dp.message_handler(content_types=['text'])
async def get_message(message):
	if message.text == "Тех. поддержка☎️":
		await bot.send_message(message.chat.id, help_msg, parse_mode='Markdown')

@dp.callback_query_handler(text="get_wth")
async def send_random_value(message: types.Message):
	class asd(StatesGroup):
		q1 = State()
	await bot.send_message(message.chat.id, "Введите название города")
	await asd.q1.set()
	@dp.message_handler(state=asd.q1)
	async def ans_q1(message: types.Message, state: FSMContext):
		answer = message.text
		await state.update_data(answer1=answer)
		data = await state.get_data()
		answer1 = data.get("answer1")
		city = transliterate.translit(answer1, reversed=True)
		param=(requests.get(openweather_token+city+"&units=metric").json())
		if param['cod'] == '404':
			await state.finish()
			await bot.send_message(message.chat.id, 'Не удалось найти город с таким названием ＞人＜；')
		else:
			temp = round(param["main"]["temp"])
			temp_f = round(param["main"]["feels_like"])
			humidity = param["main"]["humidity"]
			wind = param["wind"]["speed"]
			mw = param["weather"][0]["id"]
			mainwth = eval("f"+str(mw))
			cit = transliterate.translit(param["name"],'ru', reversed=True)
			vivod= (f"На данный момент в городе {answer1}:\n"
				f"Температура: {temp}°, ощущается как {temp_f}°\n"
				f'Влажность: {humidity}%, ветер: {wind}м/с\n'
				f'Осадки: {mainwth}')
			await bot.send_message(message.chat.id, vivod)
			await state.finish()

########################################################## Настройки ############################################################

	elif message.text == "Настройки":
		await bot.send_message(message.chat.id, 'Здесь вы можете настроить свой аккаунт', reply_markup=keyboard_settings(id))
		@dp.callback_query_handler(text="serv")
		async def sub(call: types.CallbackQuery):
			await bot.send_message(call.message.chat.id, 'Выберите сервис', reply_markup=keyboard_serv())
			@dp.callback_query_handler(text="wth")
			async def sub(call: types.CallbackQuery):
				con = sqlite3.connect('db.db')
				cur = con.cursor()
				cur = con.execute(f'SELECT id FROM subs WHERE id={message.chat.id}')
				check = cur.fetchall()
				print(check)
				if not str(message.from_user.id) in str(check):
					con.execute(f'INSERT INTO subs(id) VALUES ({message.from_user.id})')
					con.commit()
				con.close()
				await bot.send_message(call.message.chat.id, 'Хотите подписаться на рассылку погоды?', reply_markup=keyboard_danet())
				@dp.callback_query_handler(text="yes")
				async def sub(call: types.CallbackQuery):
					class wth(StatesGroup):
						wtht = State()
						wthtz = State()
						wthtown = State()
					await bot.send_message(call.message.chat.id, "Во сколько отправить вам информацию о погоде?\nНапример: 7:00")
					await wth.wtht.set()
					@dp.message_handler(state=wth.wtht)
					async def ans_qq1(message: types.Message, state: FSMContext):
						answer = message.text
						await state.update_data(answerwtht=answer)
						data = await state.get_data()
						answerwtht1 = data.get("answerwtht")
						await bot.send_message(call.message.chat.id, "Какой у вас часовой пояс?\nНапример: если UTC:+1, то +1")
						await wth.wthtz.set()
						@dp.message_handler(state=wth.wthtz)
						async def ans_qq2(message: types.Message, state: FSMContext):
							answer = message.text
							await state.update_data(answerwthtz=answer)
							data2 = await state.get_data()
							answerwthtz1 = data2.get("answerwthtz")
							await bot.send_message(call.message.chat.id, "О каком городе хотите получать информацию?")
							await wth.wthtown.set()
							@dp.message_handler(state=wth.wthtown)
							async def ans_qq3(message: types.Message, state: FSMContext):
								con = sqlite3.connect('db.db')
								cur = con.cursor()
								answer = message.text
								await state.update_data(answerwthtown=answer)
								data = await state.get_data()
								answerwthtown1 = data.get("answerwthtown")
								await bot.send_message(call.message.chat.id, "Вы успешно подписались на рассылку")
								await bot.send_message(5036976963, f"{message.from_user.id} Подписался на рассылку(Погода)")
								con.execute(f'UPDATE subs set wthsub = "yes" WHERE id={message.from_user.id}')
								con.execute(f'UPDATE subs set (wthtimee, wthtimezone) = ("{answerwtht1}", "{answerwthtz1}") WHERE id={message.from_user.id}')
								con.execute(f'UPDATE subs set wthtown = "{answerwthtown1}" WHERE id={message.from_user.id}')
								con.commit()
								await state.finish()
								con.close()
		      #except:
		       # await bot.send_message(message.chat.id, "насяльника ашибка! фастом в лобби", reply_markup=keyboard_menu())
				@dp.callback_query_handler(text="net")
				async def sub(call: types.CallbackQuery):
					await bot.send_message(message.chat.id, "Подписка на рассылку успешно отменена", reply_markup=keyboard_menu())
		@dp.callback_query_handler(text="spam")
		async def send_random_value(call: types.CallbackQuery):
			if message.chat.id == 5036976963:
				await bot.send_message(message.chat.id, 'Введите текст, который нужно разослать:')
				con = sqlite3.connect('db.db')
				cur = con.cursor()
				cur.execute("SELECT id FROM users")
				class asd(StatesGroup):
					qd1 = State()
				await asd.qd1.set()
				@dp.message_handler(state=asd.qd1)
				async def ans_q1(message: types.Message, state: FSMContext):
					con = sqlite3.connect('db.db')
					cur = con.cursor()
					answer = message.text
					await state.update_data(answer1=answer)
					data = await state.get_data()
					answer1 = data.get("answer1")
					await state.finish()
					row = cur.fetchall()
					for x in row:
						await bot.send_message(x[0], answer1)
					con.close()
			else:
				await bot.send_message(message.chat.id, 'Ты куда полез\nУ тебя админки нет')
	else:
		await bot.send_message(message.chat.id, other_type, reply_markup=keyboard_menu())
'''
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
if __name__ == '__main__':
	print('Монстр пчелы запущен!')
executor.start_polling(dp)
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################