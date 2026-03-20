from telebot import TeleBot

bot = TeleBot(token=open('s3_token.txt', 'r').read())


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Բարի գալուստ VIN կոդի ստուգման բոտ, ուղարկեք Ձեր VIN ը')


bot.polling()