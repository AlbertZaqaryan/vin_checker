from telebot import TeleBot
from dotenv import load_dotenv
import os

load_dotenv()
bot = TeleBot(token=os.getenv('TOKEN'))


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Բարի գալուստ VIN կոդի ստուգման բոտ, ուղարկեք Ձեր VIN ը')


bot.polling()