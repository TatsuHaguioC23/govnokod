# -*- coding: utf8 -*-
################################################################################################################################
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
#################################################################################################################################

######################################################################
from aiogram.dispatcher import FSMContext                            ## ТО, ЧЕГО ВЫ ЖДАЛИ - FSM
from aiogram.dispatcher.filters import Command                        ## ТО, ЧЕГО ВЫ ЖДАЛИ - FSM
from aiogram.contrib.fsm_storage.memory import MemoryStorage        ## ТО, ЧЕГО ВЫ ЖДАЛИ - FSM
from aiogram.dispatcher.filters.state import StatesGroup, State        ## ТО, ЧЕГО ВЫ ЖДАЛИ - FSM
######################################################################

######################
import config        ## ИМПОРТИРУЕМ ДАННЫЕ ИЗ ФАЙЛОВ config.py
import keyboard        ## ИМПОРТИРУЕМ ДАННЫЕ ИЗ ФАЙЛОВ keyboard.py
######################

import logging # ПРОСТО ВЫВОДИТ В КОНСОЛЬ ИНФОРМАЦИЮ, КОГДА БОТ ЗАПУСТИТСЯ

storage = MemoryStorage() # FOR FSM
bot = Bot(token=config.botkey, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    )

@dp.message_handler(Command("start"), state=None)
async def welcome(message):
    joinedFile = open("user.txt","r")
    joinedUsers = set ()
    for line in joinedFile:
        joinedUsers.add(line.strip())
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("user.txt","a")
        joinedFile.write(str(message.chat.id)+ "\n")
        joinedUsers.add(message.chat.id)
    joinedFile = open("users.txt","r")
    joinedUsers = set ()
    for line in joinedFile:
        joinedUsers.add(line.strip())
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("users.txt","a")
        joinedFile.write(str(message.chat.id)+ " --> " +str(message.from_user.first_name)+ "\n")
        joinedUsers.add(message.chat.id)


    await bot.send_message(message.chat.id, f"Дарова, *{message.from_user.first_name}*.", reply_markup=keyboard.start, parse_mode='Markdown')


@dp.message_handler(commands=['spam'])
async def rassilka(message):
    if message.chat.id == config.admin:
        await bot.send_message(message.chat.id, f"*Рассылка началась \nЯ скажу, когда докидаюсь*", parse_mode='Markdown')
        receive_users, block_users = 0, 0
        joinedFile = open ("user.txt", "r")
        joinedUsers = set ()
        for line in joinedFile:
            joinedUsers.add(line.strip())
        joinedFile.close()
        for user in joinedUsers:
            try:
                await bot.send_photo(user, open('lzt.jpg', 'rb'), message.text[message.text.find(' '):])
                receive_users += 1
            except:
                block_users += 1
            await asyncio.sleep(0.4)
        await bot.send_message(message.chat.id, f"*Рассылка завершена *\n"
                                                              f"получили сообщение: *{receive_users}*\n"
                                                              f"заблокировали бота: *{block_users}*", parse_mode='Markdown')



###################################            FSM              ###############################################
class meinfo(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()
    Q4 = State()

@dp.message_handler(Command("me"), state=None)        # Создаем команду /me для админа.
async def enter_meinfo(message: types.Message):
    if message.chat.id == config.admin:               
        await message.answer("начинаем настройку.\n"        # Бот спрашивает ссылку
                         "№1 Введите линк на ваш профиль")
        await meinfo.Q1.set()                                    # и начинает ждать наш ответ.

@dp.message_handler(state=meinfo.Q1)                                # Как только бот получит ответ, вот это выполнится
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)                            # тут же он записывает наш ответ (наш линк)

    await message.answer("Линк сохранён. \n"
                         "№2 Введите текст.")
    await meinfo.Q2.set()                                    # дальше ждёт пока мы введем текст


@dp.message_handler(state=meinfo.Q2)                    # Текст пришел а значит переходим к этому шагу
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text 
    await state.update_data(answer2=answer)                # опять же он записывает второй ответ

    await message.answer("Текст сохранён.")

    data = await state.get_data()                #
    answer1 = data.get("answer1")                # тут он сует ответы в переменную, чтобы сохранить их в "БД" и вывести в след. сообщении
    answer2 = data.get("answer2")                #

    joinedFile = open("link.txt","w", encoding="utf-8")        # Вносим в "БД" encoding="utf-8" НУЖЕН ДЛЯ ТОГО, ЧТОБЫ ЗАПИСЫВАЛИСЬ СМАЙЛИКИ
    joinedFile.write(str(answer1))
    joinedFile = open("text.txt","w", encoding="utf-8")        # Вносим в "БД" encoding="utf-8" НУЖЕН ДЛЯ ТОГО, ЧТОБЫ ЗАПИСЫВАЛИСЬ СМАЙЛИКИ
    joinedFile.write(str(answer2))

    await message.answer(f'Ваша ссылка на профиль : {answer1}\nВаш текст:\n{answer2}')    # Ну и выводим линк с текстом который бот записал
    await state.finish()

####################################### БАЛИК ####################################
@dp.message_handler(Command('balance'), state=None)
async def zxc(message: types.Message):
    if message.chat.id == config.admin:
        users1 = open('users.txt', encoding="utf-8")
        users = users1.read()
        await message.answer(f"Какому пользователю хотите подарить денюжек?\n{users}")
        await meinfo.Q3.set()
@dp.message_handler(state=meinfo.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer3=answer)
    await message.answer("Сколько денюжек подарить?")
    await meinfo.Q4.set()
@dp.message_handler(state=meinfo.Q4)
async def answer_q4(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer4=answer)
    await message.answer("Баланс пользователя пополнен на "+ answer)
    data = await state.get_data()
    answer3 = data.get('answer3')
    answer4 = data.get('answer4')
    joinedFile = open('balance.txt', 'w')
    joinedFile.write(answer3)
    joinedFile = open('balance.txt', 'w')
    joinedFile.write(answer4)

@dp.message_handler(content_types=['text'])
async def get_message(message):
    if message.text == "Информация":
        await bot.send_message(message.chat.id, text = "Сделано с любовью o(^▽^)o", parse_mode='Markdown')

    if message.text == "Статистика":
        await bot.send_message(message.chat.id, text = "Хочешь просмотреть статистику бота?", reply_markup=keyboard.stats, parse_mode='Markdown')

    if message.text == "Разработчик":
        link1 = open('link.txt', encoding="utf-8") # Вытаскиваем с нашей "БД" инфу, помещаем в переменную и выводим её
        link = link1.read()

        text1 = open('text.txt', encoding="utf-8") # Вытаскиваем с нашей "БД" инфу, помещаем в переменную и выводим её
        text = text1.read()

        await bot.send_message(message.chat.id, text = f"Создатель: {link}\n{text}", parse_mode='Markdown')

    if message.text == "Сервисы🔧":
        await bot.send_message(message.chat.id, text = "Все доступные* на данный момент сервисы:", reply_markup=keyboard.serv)

######################################## CALLBACK_DATA ########################################
@dp.callback_query_handler(text_contains='join') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def join(call: types.CallbackQuery):
    if call.message.chat.id == config.admin:
        d = sum(1 for line in open('user.txt'))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Вот статистика бота: *{d}* человек', parse_mode='Markdown')
    else:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "У тебя нет админки\nКуда ты полез", parse_mode='Markdown')

@dp.callback_query_handler(text_contains='cancle') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "cancle" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "cancle"
async def cancle(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= "Фастом в лобби", parse_mode='Markdown')

@dp.callback_query_handler(text_contains='nakr')
async def nakt(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= "Временно недоступно ಥ_ಥ")
@dp.callback_query_handler(text_contains='bomb')
async def bomb(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= "Временно недоступно ಥ_ಥ")

























##############################################################
if __name__ == '__main__':
    print('Монстр пчелы запущен!')                                    # ЧТОБЫ БОТ РАБОТАЛ ВСЕГДА с выводом в начале вашего любого текста
executor.start_polling(dp)
##############################################################