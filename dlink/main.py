import os
import time
import telebot
from telebot import types

# Set up the Telegram bot
bot = telebot.TeleBot('6115548318:AAF2Sw0DsWUUOVBKoH4VxhvAjLQJStC-zdU')

# Define a function to handle incoming files
@bot.message_handler(content_types=['document', 'video', 'audio', 'voice', 'photo'])
def handle_file(message):
    # Download the file
    file_info = bot.get_file(message.document.file_id)
    file_path = file_info.file_path
    downloaded_file = bot.download_file(file_path)

    # Generate a direct link to the file
    file_extension = os.path.splitext(file_path)[-1]
    direct_link = f'https://api.telegram.org/file/bot{bot.token}/{file_path}'

    # Save the file to the cache directory
    file_name = f'{message.document.file_id}{file_extension}'
    file_path = os.path.join(bot.cache_dir, file_name)
    with open(file_path, 'wb') as f:
        f.write(downloaded_file)

    # Send the direct link to the user
    bot.reply_to(message, direct_link)

    # Delete the file after 1 hour
    time.sleep(3600)
    os.remove(file_path)

# Start the bot
bot.polling()
