import telegram
cafe_closing_time_token = '954121948:AAECe6nbZtbfgBXd9mnRGwH7u0HZpCyvBrQ'
cafe_closing_time = telegram.Bot(token = cafe_closing_time_token)
updates = cafe_closing_time.getUpdates()
for u in updates:
    print(u.message)

import sys
import ChatBotModel

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def proc_practicing(bot, update):
    cafe_closing_time.sendMessage('어디에서 작업할 거야?')
    cafe_closing_time.sendPhoto(photo='https://telegram.org/img/t_logo.png')

def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

def set_command(bot, update):
    print("set")
    set_menu = []
    set_menu.append(InlineKeyboardButton("col1", callback_data='1이다'))
    set_menu.append(InlineKeyboardButton("col2", callback_data='2이다'))
    set_menu.append(InlineKeyboardButton("col3", callback_data='3이다'))
    set_menu_markup = InlineKeyboardMarkup(build_menu(set_menu, len(set_menu) - 1))

    update.message.reply_text("뉴스 구독을 신청하시겠습니까?", reply_markup=set_menu_markup)

    updater.dispatcher.add_handler(CommandHandler('set', set_command, pass_args=True))

def proc_start(bot, update):
    cafe_closing_time.sendMessage('안녕!')

def proc_stop(bot, update):
    cafe_closing_time.sendMessage('내일 마저 하자')
    cafe_closing_time.stop()

cafe_closing_time = ChatBotModel.BotCafe()
cafe_closing_time.add_handler('practice', proc_practicing)
cafe_closing_time.add_handler('stop', proc_stop)
cafe_closing_time.add_handler('start',proc_start)
cafe_closing_time.start()