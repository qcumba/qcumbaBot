# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from OrgInfoGenerator import OrgInfoGenerator
from OrgInfoMessage import make_org_info_message
from OrgInfoGenerator import AddressInfoGenerator
import sys

TELEGRAM_TOKEN = '219250835:AAEEvskd7ixSSyRT2jAO-g6HXW7e8ZwKS34'
DADATA_TOKEN = '962ece1f054b4f80f558b93fd4fa635692530c48'


def start(bot, update):
    user_name = update.message.from_user.first_name
    greeting_msg = u'Привет, %s! Для поиска введите фрагмент или полное название, либо ИНН.' % user_name

    bot.sendMessage(chat_id=update.message.chat_id, text=greeting_msg)


def find_org(bot, update):
    org_info_generator = OrgInfoGenerator.OrgInfoGenerator(DADATA_TOKEN)
    address_info_generator = AddressInfoGenerator.AddressInfoGenerator(DADATA_TOKEN)


    orgs_list = org_info_generator.get_org_list(update.message.text)
    location = address_info_generator.get_address_coords(orgs_list[0].address)
    reload(sys)
    sys.setdefaultencoding('utf-8')
    message = make_org_info_message(orgs_list[0])
    bot.sendMessage(chat_id=update.message.chat_id, text=message, parse_mode='HTML')
    bot.sendLocation(chat_id=update.message.chat_id, latitude=location[0].geo_lat, longitude=location[0].geo_lon)

def main():
    updater = Updater(token=TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler([Filters.text], find_org))

    # updater.start_polling()
    updater.start_webhook(listen='0.0.0.0',
                          port=8443,
                          url_path=TELEGRAM_TOKEN,
                          key='C:\Certs\private.key',
                          cert='C:\Certs\cert.pem',
                          webhook_url='https://qcumba.com:8443/%s' % TELEGRAM_TOKEN)


if __name__ == '__main__':
    main()
