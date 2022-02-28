from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

######################################################
start = types.ReplyKeyboardMarkup(resize_keyboard=True) # СОЗДАЕМ ВООБЩЕ ОСНОВУ ДЛЯ КНОПОК

bal = types.KeyboardButton("Баланс | 0₽")
serv = types.KeyboardButton("Сервисы🔧")
zak = types.KeyboardButton("Мои заказы🗂")
sett = types.KeyboardButton("Настройки🔧")
info = types.KeyboardButton("Информация")            # ДОБАВЛЯЕМ КНОПКУ ИНФОРМАЦИИ
stats = types.KeyboardButton("Статистика")            # ДОБАВЛЯЕМ КНОПКУ СТАТИСТИКИ
razrab = types.KeyboardButton("Разработчик")            # ДОБАВЛЯЕМ КНОПКУ РАЗРАБОТЧИК

start.add(serv) #ДОБАВЛЯЕМ ИХ В БОТА
start.add(bal, zak)
start.add(sett)
######################################################
######################################################
stats = InlineKeyboardMarkup()    # СОЗДАЁМ ОСНОВУ ДЛЯ ИНЛАЙН КНОПКИ
stats.add(InlineKeyboardButton(f'Да', callback_data = 'join')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
stats.add(InlineKeyboardButton(f'Нет', callback_data = 'cancle')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ

serv = InlineKeyboardMarkup()
serv.add(InlineKeyboardButton(f"Заказать накрутку🛒", callback_data = 'nakr'))
serv.add(InlineKeyboardButton(f"Бомбер💣", callback_data = 'bomb'))

settt = InlineKeyboardMarkup()
settt.add(InlineKeyboardButton(f"Информация"))
######################################################