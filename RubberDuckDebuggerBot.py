from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
import os
import random


random.seed
token = os.environ['RUBBERBOT_TOKEN']
quacks = ['QUACK'] * 20 + ['QUACK!'] * 10 + ['QUACK?'] * 6 + ['QUACK, QUACK QUACK, QUACK.', 'QUACK?!?!?', 'QUAAAAAAAAACK', 'QU-QU-QUACK?!?', 'QUAAACK', 'QUACK QUACK QUACK, QUACK?'] * 4 + ['le quack', 'I must say, your code does sound quite messy. You should probably... I mean... QUACK!']

def handle(update, context):
    r = random.randrange(len(quacks))
    context.bot.send_message(chat_id = update.effective_chat.id, text = quacks[r])

updater = Updater(token = token, use_context = True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.all, handle))

updater.start_polling()