#5806659815:AAEMRFDhJTs8lM8KOGc4JxWnP2bH7VOoAo4

import telebot
import subprocess

# Initialize the bot with your Telegram API token
bot = telebot.TeleBot("5806659815:AAEMRFDhJTs8lM8KOGc4JxWnP2bH7VOoAo4")


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

# Handler for the /store command
@bot.message_handler(commands=['store'])
def store_file(message):
    # Get the file from the message
    file = message.document.file_id

    # Download the file
    downloaded_file = bot.download_file(bot.get_file(file).file_path)

    # Save the file to disk
    with open("filename.extension", "wb") as f:
        f.write(downloaded_file)

    # Send a confirmation message
    bot.reply_to(message, "File stored successfully!")

# Start the bot
bot.polling()