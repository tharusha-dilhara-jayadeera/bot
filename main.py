import os
import telebot


bot = telebot.TeleBot("5143362253:AAH28kD97_ygPePbOJr7n8mSZHxNQ8WDyh0")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm Uvindu Bro Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "https://youtube.com/c/Uvindubro")



bot.polling()
