# -*- coding: utf-8 -*-
from emoji import emojize
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from OrgInfoGenerator import OrgInfoGenerator
from OrgInfoMessage import make_org_info_message
from OrgInfoGenerator import AddressInfoGenerator
import Settings.Settings
import sys
import logging


TELEGRAM_TOKEN = Settings.Settings.get_setting_value('telegram_token')


logging.basicConfig(level=logging.INFO,
                    filename='log_bot.txt',
                    format='%(asctime)s - %(levelname)s - %(message)s')
reload(sys)
sys.setdefaultencoding('utf-8')


def start(bot, update):
    user_name = update.message.from_user.first_name
    greeting_msg = u'Привет, %s!' \
                   u'Для поиска введите фрагмент или полное название, либо ИНН.' % user_name

    bot.sendMessage(chat_id=update.message.chat_id, text=greeting_msg)


def find_org(bot, update):
    org_info_generator = OrgInfoGenerator.OrgInfoGenerator()
    address_info_generator = AddressInfoGenerator.AddressInfoGenerator()

    orgs_list = org_info_generator.get_org_list(update.message.text)
    location = address_info_generator.get_address_coords(orgs_list[0].address)

    buttons = [[InlineKeyboardButton(text='Следующий результат', callback_data=str(orgs_list[1].id))]]

    message = make_org_info_message(orgs_list[0])

    bot.sendMessage(chat_id=update.message.chat_id, text=message, parse_mode='HTML')
    bot.sendLocation(chat_id=update.message.chat_id,
                     latitude=location[0].latitude, longitude=location[0].longitude,
                     reply_markup=InlineKeyboardMarkup(buttons))


def get_other_result(bot, update):
    bot.sendMessage(chat_id=update.callback_query.message.chat_id, text=update.callback_query.data)


def main():
    logging.info('Bot started')
    updater = Updater(token=TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler([Filters.text], find_org))
    dispatcher.add_handler(CallbackQueryHandler(get_other_result))

    # updater.start_polling()
    try:
        updater.start_webhook(listen='0.0.0.0',
                              port=8443,
                              url_path=TELEGRAM_TOKEN,
                              key='C:\Certs\private.key',
                              cert='C:\Certs\cert.pem',
                              webhook_url='https://qcumba.com:8443/%s' % TELEGRAM_TOKEN)
    except Exception, e:
        logging.error('Error occurred! More info: %s' % e.message)

if __name__ == '__main__':
    main()
