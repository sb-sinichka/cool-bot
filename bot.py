import telebot

from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler()
def echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling()
