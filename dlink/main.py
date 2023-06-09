"""
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

bot.polling()
"""

import telebot
import requests
from bs4 import BeautifulSoup
import time

# replace YOUR_API_TOKEN with your Telegram bot API token
bot = telebot.TeleBot('6097684986:AAEHbipv0Sv0hm9LOV7qqZbomHstElFD6Pk')
admin_id = '5214644649'

# Send a welcome message when the bot is started.
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! I will notify you when there are new free Udemy courses available.")

# Function to get the latest free Udemy courses.
def get_free_course():
    url = 'https://www.real.discount/udemy-coupon/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    course_list = soup.find_all('div', {'class': 'coupon-name'})
    
    for course in course_list:
        coupon = course.find_next_sibling('div', {'class': 'coupon-code'}).text.strip()
        link = course.find('a').get('href')
        message = f"New free Udemy course: {link}\nCoupon code: {coupon}"
        bot.send_message(admin_id, message)

# Run the function every hour to check for new coupons.
while True:
    get_free_course()
    time.sleep(3600)

# Start polling for messages from users.
print ("Deployed")
bot.polling()
