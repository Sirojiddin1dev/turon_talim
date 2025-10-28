import telebot
from .models import TelegramAdmin

TOKEN = "5678987654678:ddcgfgdgffdgdfgdfgfdg"

bot = telebot.TeleBot(TOKEN)


def send_message_admin(message):
    try:
        for i in TelegramAdmin.objects.all():
            bot.send_message(i.telegram_id, message)
        return True
    except:
        return False