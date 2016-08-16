# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler

TOKEN = ''


def start(bot, update):
    user_name = update.message.from_user.first_name
    greeting_msg = u'Привет, %s! Для поиска введите фрагмент или полное название, либо ИНН.' % user_name

    bot.sendMessage(chat_id=update.message.chat_id, text=greeting_msg)


def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    updater.start_polling()


if __name__ == '__main__':
    main()
