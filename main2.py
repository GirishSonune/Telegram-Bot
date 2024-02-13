import telegram.ext
from dotenv import load_dotenv
import os
import logging
from telegram.ext import Updater

load_dotenv()
TOKEN = os.getenv("TOKEN")

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    update.message.reply_text("Hello! Welcome Girish... ")

def helps(update, context):
    help_message = """
    Hi there, This Bot is Created By Girish Sonune.
    How can I help you?...

    /start - To start the conversation
    /content - Information about This Bot and Owner.
    /contact - Information about contact of Girish.
    /help - To get this help Menu.

    I hope this helps you :)
    """
    update.message.reply_text(help_message)

def content(update, context):
    content_message = """
    This Bot is Created By Girish Sonune During the Vacation of Diwali...

    Being a first-generation immigrant in India has significantly influenced my distinct viewpoints and ambitions. I possess a natural curiosity for acquiring new knowledge and enjoy the process of learning.

    Life has instilled in me the value of pursuing opportunities, regardless of their level of risk. My professional journey commenced with a Bachelor's degree in Information Technology. I have a passion for exploring the world and capturing moments through photography.

    Please feel free to contact me via LinkedIn. I'm always looking forward to an insightful conversation over tea!
    """
    update.message.reply_text(content_message)

def contact(update, context):
    contact_message = """
    You can connect with me on:
    Linktree: https://linktr.ee/girishsonune
    Portfolio: https://girishsonune.github.io/New-Portfolio/
    LinkedIn: https://www.linkedin.com/in/girish-sonune-7a7090255
    GitHub: https://github.com/GirishSonune
    Twitter: https://twitter.com/GirishSonune?t=5vldDBscsdJYUqxFj4srKw&s=09
    Instagram: https://instagram.com/girish_sonune?utm_source=qr&igshid=MzNlNGNkZWQ4Mg%3D%3D
    Facebook: https://www.facebook.com/profile.php?id=100094754221514&mibextid=ZbWKwL
    """
    update.message.reply_text(contact_message)

def handle_message(update, context):
    update.message.reply_text(f"You said: {update.message.text}")

# Create the Updater and pass it the bot's token
updater = telegram.ext.Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Register command handlers
dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('help', helps))
dispatcher.add_handler(telegram.ext.CommandHandler('content', content))
dispatcher.add_handler(telegram.ext.CommandHandler('contact', contact))

# Register a message handler to reply to any text messages
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.TEXT & telegram.ext.Filters.MENTION, handle_message))

try:
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()
except Exception as e:
    logging.error(f"Error: {e}")
