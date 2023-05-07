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

# Handler for the /shell command 
@bot.message_handler(commands=['shell']) 
def shell_command(message): 
    # Get the command from the message 
    command = message.text.split('/shell')[1].strip() 

    # Start the process and get the output 
    try: 
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) 
        for line in iter(process.stdout.readline, b''): 
            bot.send_message(chat_id=message.chat.id, text=line.decode()) 
    except Exception as e: 
        bot.reply_to(message, f"Error: {e}") 

# Handler for the /kali command 
@bot.message_handler(commands=['kali']) 
def kali_command(message): 
    # Get the command from the message 
    command = message.text.split('/kali')[1].strip() 

    # Start the process and get the output 
    try: 
        process = subprocess.Popen(f"kali {command}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) 
        for line in iter(process.stdout.readline, b''): 
            bot.send_message(chat_id=message.chat.id, text=line.decode()) 
    except Exception as e: 
        bot.reply_to(message, f"Error: {e}") 

# Handler for the /bash command 
@bot.message_handler(commands=['bash']) 
def bash_command(message): 
    # Get the command from the message 
    command = message.text.split('/bash')[1].strip() 

    # Start the process and get the output 
    try: 
        process = subprocess.Popen(f"bash -c '{command}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) 
        for line in iter(process.stdout.readline, b''): 
            bot.send_message(chat_id=message.chat.id, text=line.decode()) 
    except Exception as e: 
        bot.reply_to(message, f"Error: {e}") 

# Handler for the /stop command 
@bot.message_handler(commands=['stop']) 
def stop_command(message): 
    # Stop the process 
    process.terminate() 

# Define the custom keyboard 
keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2) 
shell_button = telebot.types.KeyboardButton('/shell') 
kali_button = telebot.types.KeyboardButton('/kali') 
bash_button = telebot.types.KeyboardButton('/bash') 
stop_button = telebot.types.KeyboardButton('/stop') 
keyboard.add(shell_button, kali_button, bash_button, stop_button) 

# Define the handler for the /keyboard command 
@bot.message_handler(commands=['keyboard']) 
def keyboard_command(message): 
    # Send the custom keyboard 
    bot.send_message(chat_id=message.chat.id, text='Choose a command:', reply_markup=keyboard) 

# Start the bot 
bot.polling()
