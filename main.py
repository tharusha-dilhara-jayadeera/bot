import os
import telebot

bot = telebot.TeleBot("5143362253:AAH28kD97_ygPePbOJr7n8mSZHxNQ8WDyh0")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.replly_to(message,"Welcome , bot weda ")


@bot.message_handler(commands=["how"])
def send_message(message):
    bot.send_message(message,"how wede hari")


bot.polling()
