import os
import telebot

bot = telebot.TeleBot("api key")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.replly_to(message,"Welcome , bot weda ")


@bot.message_handler(commands=["how"])
def send_message(message):
    bot.send_message(message,"how wede hari")


bot.polling()