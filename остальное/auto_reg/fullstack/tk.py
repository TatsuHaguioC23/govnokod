from tkinter import *
import os
import shutil
import time
from tkinter import ttk
from tkinter import messagebox as mb
from PIL import ImageTk, Image
#################################################################################################################################
########################################################### Переменные ##########################################################
#################################################################################################################################
### ЦВЕТА
#1d1d1d
#121212
#5B04BC
def open_img():
	img = ImageTk.PhotoImage(Image.open("captcha.jpg"))
	panel = Label(window, image=img)
	panel.image = img
	panel.place(relx=.76, rely=.15)
#################################################################################################################################
#################################################### Интерфейс программы ########################################################
#################################################################################################################################
window = Tk()
window.title("Авторег")
window.iconbitmap('favicon.ico')
window['bg'] = '#121212'
#Разрешение монитора по дефолту
normal_width = 1920
normal_height = 1080
#Узнаём разрешение монитора
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
#Подгоняем под монитор
percentage_width = screen_width / (normal_width / 100)
percentage_height = screen_height / (normal_height / 100)
scale_factor = ((percentage_width + percentage_height) / 2) / 100
#Размер шрифта
fontsize = int(25 * scale_factor)
minimum_size = 10
if fontsize < minimum_size:
		fontsize = minimum_size
fontsizeHding = int(20 * scale_factor)
minimum_size = 10
if fontsizeHding < minimum_size:
		fontsizeHding = minimum_size
#Настройки кнопок
default_style = ttk.Style()
default_style.configure('New.TButton', font=("", fontsize))
#################################################################################################################################
########################################################### Текст ###############################################################
#################################################################################################################################
info = Label(window, text="Авторег почт by AbssDuo", font=("Lucida Console", fontsizeHding), fg="white", bg="#121212")
info.place(relx = .015, rely = .015)
kolvot = Label(window, text="Введите количество\nсоздаваемых почт", font=("Lucida Console", fontsizeHding), fg="white", bg="#121212")
kolvot.place(relx=.03,rely=.62)
servt = Label(window, text="Выберите сервис", font=("Lucida Console", fontsizeHding), fg="white", bg="#121212")
servt.place(relx=.28,rely=.636)
serv = Button(window, text="@mail.ru", font=(fontsize), fg="#5B04BC", bg="#121212", borderwidth=0, activebackground="#121212")
serv.place(relx=.295, rely=.7, relwidth=.12, relheight=.025)
start = Button(window, text="Запустить", font=("Lucida Console", fontsizeHding), fg="#5B04BC", bg="#1d1d1d", borderwidth=0, activebackground="#5B04BC", command=open_img)
start.place(relx=.06, rely=.3, relwidth=.33, relheight=.06)
kolvo = Entry(window, font=("xz", fontsize), fg="#5B04BC", bg="#1d1d1d", borderwidth=0)
kolvo.place(relx=.065,rely=.7,relwidth=.1,relheight=.05)
captchat = Label(window, text="Здесь будет появляться капча", font=("Lucida Console", 15), fg="white", bg="#121212")
captchat.place(relx=.7, rely=.09)
captchaE = Entry(window, font=("Lucida Console", 15), fg="#5B04BC", bg="#1d1d1d", borderwidth=0)
captchaE.place(relx=.7, rely=.3,relwidth=.17,relheight=.04)
captchab = Button(window, text="Отправить", font=("Lucida Console", 13), command=, fg="#5B04BC", bg="#1d1d1d", activebackground="#5B04BC", borderwidth=0)
captchab.place(relx=.88, rely=.3,relwidth=.1,relheight=.04)
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################







#Запуск окна
window.geometry('1280x720+0+200')
window.mainloop()