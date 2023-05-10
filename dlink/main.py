#bot = ('6115548318:AAF2Sw0DsWUUOVBKoH4VxhvAjLQJStC-zdU'
import telebot
import requests
import os

TOKEN = '6115548318:AAF2Sw0DsWUUOVBKoH4VxhvAjLQJStC-zdU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to my dlink bot, Send me file and I will give u direct download link.")

@bot.message_handler(content_types=['document', 'video', 'audio', 'photo'])
def handle_file(message):
    file_info = bot.get_file(message.document.file_id)
    file_url = f'https://api.telegram.org/file/bot{TOKEN}/{file_info.file_path}'
    bot.reply_to(message, f"Here is ur download link: {file_url}")
    os.remove(file_url)

bot.polling()
