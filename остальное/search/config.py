#################################################################################################################################
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import logging
import keyboard
#################################################################################################################################
#################################################################################################################################
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
#################################################################################################################################
################################################################################################################################
telegram_token = '5121775845:AAHtEdiHkLqBMIaBz_aX8jK1SVEWOWEb7ks'
openweather_token = "http://api.openweathermap.org/data/2.5/weather?appid=1840343a10e12bec9837aca471c28ced&q="
################################################################################################################################
admins = [5036976963]
################################################################################################################################
supports = 'ТГ: https://t.me/abssduo Сайт: https://abssduo.tk/'  # контакты тех.поддержки
help_msg = f'Что-то сломалось или появились вопросы?\nТы всегда можешь обратиться к нам по контактам:\n{supports}' # Сообщение при /help
msg_menu = '<b>first_name</b>, Я вывел тебе кнопки, что бы мог пользоваться ботом.'  # Главное меню
msg_support = f'Наши контакты для связи {supports}'  # Тех. поддержка
other_type = 'Ничего не понял🧐, но на всякий случай переведу Вас в меню'  # Если человек отравил не текст





"""
    id — уникальный идентификатор пользователя в Telegram
    last_name — значение поля фамилия, может быть пустым
    first_name — значение поля имя, может быть пустым
    username — уникальное значение текстовый идентификатор, может быть пустым
    language_code — кодовое обозначение выбранного языка интерфейса приложения (en, ru . )
    is_bot — флаг, определяющий пользователя как бота, в случае с ботом равен 1, в случае с пользователем пустое значение
"""
############# НУЖНО ДОРАБОТАТЬ ###########
"""
				@dp.callback_query_handler(text_contains='da')
				async def cancle(call: types.CallbackQuery):
					param=(requests.get(openweather_token+city+"&units=metric").json())
					await state.finish()
					if param['cod'] == '404':
						await bot.send_message(message.chat.id, 'Не могу найти этот ваш город ＞人＜；')
						await bot.send_message(message.chat.id, 'Хотите написать на нас заявление?', reply_markup=keyboard_danet2())
						await state.finish()
						if message.text == 'да':
							await bot.send_message(message.chat.id, msg_support)
						if message.text == 'нет':
							await bot.send_message(message.chat.id, 'Спасибо (´▽`ʃ♡ƪ)')
					else:
						temp = round(param["main"]["temp"])
						temp_f = round(param["main"]["feels_like"])
						cit = transliterate.translit(param["name"],'ru', reversed=True)
						vivod= (f"На данный момент в городе {answer1}:\n"
							f"Температура: {temp}, ощущается как {temp_f}")
						await bot.send_message(message.chat.id, vivod)
						await state.finish()
"""