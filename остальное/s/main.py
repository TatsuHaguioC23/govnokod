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
import datetime
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
########################################################### Клавиатуры ##########################################################
#################################################################################################################################
def kb_menu():
	keyboard = types.InlineKeyboardMarkup(row_width=2)
	sv = {'Погода': 'get_wth', 'Настройки': 'settings', 'Тех. поддержка☎️': 'tp'}
	for zxc in sv:
		keyboard.insert(InlineKeyboardButton(zxc, callback_data=sv[zxc]))
	return keyboard
def kb_settings(id):
	keyboard = types.InlineKeyboardMarkup(row_width=2)
	sv = {'Сервисы': 'services', }
	for zxc in sv:
		keyboard.insert(InlineKeyboardButton(zxc, callback_data=sv[zxc]))
	keyboard.add(InlineKeyboardButton('◀️Назад', callback_data='menu'))

	if id in admins:
		services = {'': '_', 'Рассылка': 'spam','Выдать баланс': 'givebal', 'Забрать баланс': 'takebal'}
		keyboard.add(InlineKeyboardButton('➖➖➖➖Админ панель➖➖➖➖', callback_data='_'))
		for zxc in services:
			keyboard.insert(InlineKeyboardButton(zxc, callback_data=services[zxc]))
	return keyboard

def kb_services():
	keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
	sv = {'Погода': 'settings_wth', 'Астрономическая картинка': 'nasa', '◀️Назад': 'menu'}
	for zxc in sv:
		keyboard.insert(InlineKeyboardButton(zxc, callback_data=sv[zxc]))
	return keyboard
def kb_wth_yn():
	keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
	sv = {'Да': 'wth_yes', 'Нет': 'wth_no'}
	for zxc in sv:
		keyboard.insert(InlineKeyboardButton(zxc, callback_data=sv[zxc]))
	return keyboard
def kb_to_menu():
	keyboard = InlineKeyboardMarkup()
	keyboard.insert(InlineKeyboardButton('В меню', callback_data='menu'))
	return keyboard
def kb_wth_yn2():
	keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
	sv = {'Да': 'wth_yes2', 'Нет': 'wth_no2'}
	for zxc in sv:
		keyboard.insert(InlineKeyboardButton(zxc, callback_data=sv[zxc]))
	return keyboard
#################################################################################################################################
########################################################### Стейты(FSM) #########################################################
#################################################################################################################################
class asd(StatesGroup):
	q1 = State()
	q2 = State()
	q3 = State()
	q4 = State()
	q5 = State()
	q6 = State()
	q7 = State()
	q8 = State()
	q9 = State()
	wtht = State()
	wthtz = State()
	wthtown = State()
	spam = State()
#################################################################################################################################
########################################################### Команды #############################################################
#################################################################################################################################
@dp.message_handler(commands="start")
async def start(message: types.Message):
	con = sqlite3.connect('db.db')
	cur = con.cursor()
	cur.execute('SELECT id FROM users')
	u = cur.fetchall()
	if not str(message.from_user.id) in str(u):
		await bot.send_message(-1001626155695, f'Новый чел\nid: {message.from_user.id} username: {message.from_user.username} ({message.from_user.first_name} {message.from_user.last_name})')
		con.execute(f'INSERT INTO users(id) VALUES ({message.from_user.id})')
		con.commit()
		con.close()
		print(message.from_user.language_code)
	start_message = f'Привет, {message.from_user.first_name} 👋.\nБот постоянно дополняется всякими штуками.\nЕсли хочешь предложить что-нибудь, то можешь написать нам.'
	await bot.send_message(message.chat.id, start_message, reply_markup=kb_menu())
@dp.message_handler(commands="allinfo")
async def allinfo(message: types.Message):
	con = sqlite3.connect('db.db')
	cur = con.cursor()
	cur.execute('SELECT * FROM users')
	y = cur.fetchall()
	cur.execute('SELECT * FROM subs')
	u = cur.fetchall()
	cur.execute('SELECT * FROM spam')
	i = cur.fetchall()
	cur.execute(f'SELECT wthtown FROM subs')
	d = cur.fetchall()
	for x in d:
		await bot.send_message(5036976963, x[0])
	con.close()
	await bot.send_message(message.from_user.id, text=f"Таблица users:\n{y}\nТаблица subs:\n{u}\nТаблица spam:\n{i}")
	con.close()
#################################################################################################################################
########################################################### Не команды :) #######################################################
#################################################################################################################################
@dp.callback_query_handler(text="tp")
async def send_random_value(call: types.CallbackQuery):
	await call.message.answer(text=help_msg, parse_mode='Markdown')
@dp.callback_query_handler(text="get_wth")
async def send_random_value(call: types.CallbackQuery):
	await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Введите название города")
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
			await call.message.answer(text='Не удалось найти город с таким названием ＞人＜；', reply_markup=kb_to_menu())
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
			await call.message.answer(text=vivod, reply_markup=kb_to_menu())
			await state.finish()
@dp.callback_query_handler(text='nasa')
async def get_settings(call: types.CallbackQuery):
	await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="")

@dp.callback_query_handler(text="settings")
async def get_settings(call: types.CallbackQuery):
	await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Здесь вы можете настроить свой аккаунт", reply_markup=kb_settings(call.from_user.id))

@dp.callback_query_handler(text="services")
async def get_services(call: types.CallbackQuery):
	await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите сервис", reply_markup=kb_services())

@dp.callback_query_handler(text="spam")
async def get_spam(call: types.CallbackQuery):
	await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Введите текст, который нужно разослать:")
	await asd.spam.set()
@dp.message_handler(state=asd.spam)
async def ads_spam(message: types.Message, state: FSMContext):
	con = sqlite3.connect('db.db')
	cur = con.cursor()
	cur.execute("SELECT id FROM users")
	answer = message.text
	await state.update_data(spam_text=answer)
	data = await state.get_data()
	spam_text = data.get("spam_text")
	await state.finish()
	row = cur.fetchall()
	for x in row:
		await bot.send_message(x[0], spam_text)
	con.close()
	await bot.send_message(message.from_user.id, 'Спам рассылка завершена', reply_markup=kb_to_menu())
@dp.callback_query_handler(text="menu")
async def mune(call: types.CallbackQuery):
	await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=msg_menu, reply_markup=kb_menu())
#################################################################################################################################
########################################################### Настройки Погоды ####################################################
#################################################################################################################################
@dp.callback_query_handler(text="settings_wth")
async def get_settings_wth(call: types.CallbackQuery):
	con = sqlite3.connect('db.db')
	cur = con.cursor()
	cur = con.execute(f'SELECT id FROM subs WHERE id={call.from_user.id}')
	check = cur.fetchall()
	if not str(call.from_user.id) in str(check):
		con.execute(f'INSERT INTO subs(id) VALUES ({call.from_user.id})')
		con.commit()
	curr = con.execute(f'SELECT wthsub FROM subs WHERE id={call.from_user.id}')
	ff = curr.fetchone()
	print(ff[0])
	if ff[0] == "yes":
		await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вы уже подписаны на рассылку. Хотите отписаться от рассылки погоды?", reply_markup=kb_wth_yn2(), parse_mode='Markdown')
	else:
		await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="На данный момент нет смысла от него\nХотите подписаться на рассылку погоды?", reply_markup=kb_wth_yn(), parse_mode='Markdown')
@dp.callback_query_handler(text="wth_yes")
async def wth_y(call: types.CallbackQuery):
	await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Во сколько отправить вам информацию о погоде?\nНапример: 7:00", parse_mode='Markdown')
	await asd.wtht.set()
@dp.message_handler(state=asd.wtht)
async def ans_qq1(message: types.Message, state: FSMContext):
	answer = message.text
	await state.update_data(answerwtht=answer)
	await bot.send_message(message.from_user.id, text="Какой у вас часовой пояс?\nНапример: Москва = UTC:+3 ==> +3", parse_mode='Markdown')
	await asd.wthtz.set()
@dp.message_handler(state=asd.wthtz)
async def ans_qq2(message: types.Message, state: FSMContext):
	answer = message.text
	await state.update_data(answerwthtz=answer)
	await bot.send_message(message.from_user.id, text="О каком городе хотите получать информацию?", parse_mode='Markdown')
	await asd.wthtown.set()
@dp.message_handler(state=asd.wthtown)
async def ans_qq3(message: types.Message, state: FSMContext):
	con = sqlite3.connect('db.db')
	cur = con.cursor()
	answer = message.text
	await state.update_data(answerwthtown=answer)
	data = await state.get_data()
	answerwtht = data.get("answerwtht")
	answerwthtz = data.get("answerwthtz")
	answerwthtown = data.get("answerwthtown")
	await bot.send_message(message.from_user.id, text="Вы успешно подписались на рассылку!", parse_mode='Markdown')
	time.sleep(1)
	await bot.send_message(message.from_user.id, text=msg_menu, reply_markup=kb_menu(), parse_mode='Markdown')
	await bot.send_message(-1001626155695, text=f"{message.from_user.id} Подписался на рассылку(Погода)", parse_mode='Markdown')
	con.execute(f'UPDATE subs set wthsub = "yes" WHERE id={message.from_user.id}')
	con.execute(f'UPDATE subs set (wthtimee, wthtimezone) = ("{answerwtht}", "{answerwthtz}") WHERE id={message.from_user.id}')
	con.execute(f'UPDATE subs set wthtown = "{answerwthtown}" WHERE id={message.from_user.id}')
	con.commit()
	await state.finish()
	con.close()
@dp.callback_query_handler(text="wth_no")
async def wth_n(call: types.CallbackQuery):
	await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Процесс подписки на утренную рассылку отменён", reply_markup=kb_to_menu())
@dp.callback_query_handler(text="wth_yes2")
async def wth_y2(call: types.CallbackQuery):
	con = sqlite3.connect('db.db')
	cur = con.cursor()
	cur.execute(f'UPDATE subs set wthsub = "no" WHERE id={call.from_user.id}')
	con.commit()
	await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Подписка на рассылку погоды успешно отозвана!', reply_markup=kb_to_menu())
	con.close()
@dp.callback_query_handler(text="wth_no2")
async def wth_n2(call: types.CallbackQuery):
	con = sqlite3.connect('db.db')
	cur = con.cursor()
	cur.execute(f'UPDATE subs set wthsub = "no" WHERE id={call.from_user.id}')
	con.commit()
	await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='хз', reply_markup=kb_to_menu())
	con.close()
#################################################################################################################################

"""
async def wthhspam():
	con = sqlite3.connect('db.db')
	cur = con.cursor()
	con.execute(f'SELECT id FROM subs WHERE wthsub="yes"')
	ids = cur.fetchall()
	con.execute(f'SELECT wthtown FROM subs')
	towns = cur.fetchall()
	for x in ids:
		print(x[0])
		city = transliterate.translit(towns[0], reversed=True)
		param=(requests.get(openweather_token+city+"&units=metric").json())
		temp = round(param["main"]["temp"])
		temp_f = round(param["main"]["feels_like"])
		humidity = param["main"]["humidity"]
		wind = param["wind"]["speed"]
		mw = param["weather"][0]["id"]
		mainwth = eval("f"+str(mw))
		cit = transliterate.translit(param["name"],'ru', reversed=True)
		vivod= (f"На данный момент в городе {towns}:\n"
				f"Температура: {temp}°, ощущается как {temp_f}°\n"
				f'Влажность: {humidity}%, ветер: {wind}м/с\n'
				f'Осадки: {mainwth}')
		await bot.send_message(x[0], text=vivod)
	con.close()
"""
@dp.message_handler(commands="test")
async def xz(message: types.Message):
	con = sqlite3.connect('db.db')
	cur = con.cursor()
	cur.execute(f'SELECT wthtimee from subs WHERE wthsub="yes"')
	time = cur.fetchall()
	cur.execute(f'SELECT wthtimezone from subs WHERE wthsub="yes"')
	timezone = cur.fetchall()
	for x in time:

		d = x[0]
		x = datetime.datetime.now()
		y = x + datetime.timedelta(hours=2)
		h = "18:57"
		h = datetime.datetime.strptime(h, '%H:%M')
		print(h.strftime("%H:%M"))
		#print(dj.strftime("%H:%M"))
		#await bot.send_message(5036976963, text=f)
	con.close()
#################################################################################################################################
########################################################### Запуск бота #########################################################
#################################################################################################################################
if __name__ == '__main__':
	print('Монстр пчелы запущен!')
	executor.start_polling(dp)
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################