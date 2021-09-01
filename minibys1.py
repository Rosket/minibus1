#Импорт библиотеки
import telebot
#для создания кнопок
from telebot import types
bot = telebot.TeleBot("")#Токен из телеграмма
@bot.message_handler(content_types=['text'])#Обращение к финкции которая обрабатывает сообщения
def get_text_messages(message):
    # Если написали «Привет»
     if message.text == "Привет"or message.text == "привет" or message.text == "ghbdtn":
        #  Выводит сообщение с твоим именем
         bot.send_message(message.chat.id, 'Привет, {0.first_name}!И куда это мы собрались? 🚀'.format(message.from_user))
        # Готовим кнопки
         keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого маршрута
         key_brovki = types.InlineKeyboardButton(text='485 Минск-Бровки', callback_data='route')#название кнопки и создание ее
        # И добавляем кнопку на экран
         keyboard.add(key_brovki)#выводит кнопки на экран
         key_samah= types.InlineKeyboardButton(text='493 ДС Дружная—Cамохваловичи ', callback_data='route')#название кнопки и создание ее
         keyboard.add(key_samah)#выводит кнопки на экран
         # Показываем все кнопки сразу и пишем сообщение о выборе
         bot.send_message(message.from_user.id, text='Выбери напрвление🚩', reply_markup=keyboard)
     # Если напишешь /help
     elif message.text == "/help":
         bot.send_message(message.from_user.id, "Напиши Привет")
         # Если будет чтото кроме "привет"
     else:
         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
#опрос сервера и выдача ответа и кнопок
bot.polling(none_stop=True, interval=0)