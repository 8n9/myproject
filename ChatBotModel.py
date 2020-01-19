import telegram
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


class TelegramBot:
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token, use_context=True)
        self.id = 790714599
        self.name = name

    def sendMessage(self, text, reply_markup=None):
        self.core.sendMessage(chat_id = self.id, text=text, reply_markup=reply_markup)
    def sendPhoto(self, photo):
        self.core.sendPhoto(chat_id = self.id, photo=photo)

    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()

class BotCafe(TelegramBot):
    def __init__(self):
        self.token = #####
        TelegramBot.__init__(self, '카페영업시간', self.token)
        self.updater.stop()



    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def start(self):
        self.sendMessage('어디를 가볼까!!!')
        self.updater.start_polling()
        self.updater.idle()
