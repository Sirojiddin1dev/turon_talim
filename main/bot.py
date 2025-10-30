import telebot
from .models import TelegramAdmin

TOKEN = "8371298483:AAFhtW9FQZdXAYNjbuHpVgL1RrbB-6mQ_NQ"

bot = telebot.TeleBot(TOKEN)


def send_message_admin(message):
    try:
        for i in TelegramAdmin.objects.all():
            bot.send_message(i.telegram_id, message)
        return True
    except:
        return False