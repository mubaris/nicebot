import os
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging
import random

TOKEN = os.environ.get('NICE_BOT_TOKEN')

bot = telegram.Bot(token=TOKEN)

updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a Nice Bot, I'm Nice!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

stickers = [
        'CAADBQADbwADu4lFFU45B7At1kPCAg',
        'CAADBQADXgADu4lFFVbgRP9UIz_WAg',
        'CAADBQADXwADu4lFFZqTgNQkaxzHAg',
        'CAADBQADYAADu4lFFanQWCLRtlUdAg',
        'CAADBQADYQADu4lFFeQpDPuz-26-Ag',
        'CAADBQADYgADu4lFFferv8gMeeF4Ag',
        'CAADBQADYwADu4lFFSFYMjGcfW1zAg',
        'CAADBQADZAADu4lFFU8eSm8szf_GAg',
        'CAADBQADZQADu4lFFcZG-J3yzwb7Ag',
        'CAADBQADZgADu4lFFblaoIMt7CTHAg',
        'CAADBQADZwADu4lFFWJ3pAABP2Rs4gI',
        'CAADBQADaAADu4lFFZliuS8f9CGNAg',
        'CAADBQADaQADu4lFFTgoaNY-EtkOAg',
        'CAADBQADagADu4lFFZ8yr8TqIV02Ag',
        'CAADBQADbAADu4lFFf3yFpKuM_aPAg',
        'CAADBQADawADu4lFFdA-Io-sE6NFAg',
        'CAADBQADbgADu4lFFc-8y9XjjDr1Ag',
        'CAADBQADcAADu4lFFZvc3-50CvgQAg',
        'CAADBQADcQADu4lFFZBVEDxcGqKfAg',
        'CAADBQADcgADu4lFFbSyCQJu9GzuAg',
        'CAADBQADdAADu4lFFcMr2rqj5UKkAg',
        'CAADBQADegADu4lFFXsVSn42kIJTAg',
        'CAADBQADhQADu4lFFQABDR9L-ErvyQI'
    ]



def nice(bot, update):
    if (( 'nice' in update.message.text.lower()) and len(update.message.text) < 10):
        r = random.random()
        if ('not' in update.message.text.lower()):
            if r > 0.5:
                bot.send_message(chat_id=update.message.chat_id, text='Not Nice! 👎')
            else:
                bot.send_sticker(chat_id=update.message.chat_id, sticker='CAADBQADcwADu4lFFc6JpuBc-9waAg')
        else:
            if r > 0.5:
                bot.send_message(chat_id=update.message.chat_id, text='Nice! 👌')
            else:
                sticker = random.choice(stickers)
                bot.send_sticker(chat_id=update.message.chat_id, sticker=sticker)

echo_handler = MessageHandler(Filters.text, nice)
dispatcher.add_handler(echo_handler)

updater.start_polling()


