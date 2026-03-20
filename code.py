from telebot import TeleBot
from dotenv import load_dotenv
import os

# Загружаем переменные окружения из .env
load_dotenv()
bot = TeleBot(token=os.getenv('TOKEN'))


# Стартовое приветствие
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        'Բարի գալուստ VIN կոդի ստուգման բոտ, ուղարկեք Ձեր VIN-ը'
    )


# Обработка любых текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_vin(message):
    vin = message.text.strip()
    
    # Тут можно добавить проверку VIN или отправку запроса к API
    # Для примера просто отправим обратно введённый VIN
    response = f"Вы отправили VIN: {vin}\nԲոտը ստացել է Ձեր VIN-ը։"
    
    bot.send_message(message.chat.id, response)


# Запуск бота
bot.polling()