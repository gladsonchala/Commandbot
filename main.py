#6067882954:AAFO86WP_fdXNCTmgNqUJ7AmN7N3AW5PKfI

import telebot
import subprocess

# Initialize the bot with your Telegram API token
bot = telebot.TeleBot("6067882954:AAFO86WP_fdXNCTmgNqUJ7AmN7N3AW5PKfI")


# Define the welcome message
welcome_message = 'Welcome to the Cmd Bot!'

# Define the handler for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.chat.id
    bot.reply_to(message, welcome_message)

# Handler for the /run command
@bot.message_handler(commands=['run'])
def run_command(message):
    # Get the command from the message
    command = message.text.split('/run')[1].strip()

    # Start the process and get the output
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in iter(process.stdout.readline, b''):
            bot.send_message(chat_id=message.chat.id, text=line.decode())
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

# Start the bot
bot.polling()