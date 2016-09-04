# -*- coding: utf-8 -*-
import atexit
import sys
import traceback

import telegram
from emoji import emojize
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

import Settings.Settings
from DataBaseManager.DataBaseManager import insert_org_list, get_org
from Logger.Logger import Logger
from OrgInfoGenerator import OrgInfoGenerator
from OrgInfoMessage import make_org_info_message

TELEGRAM_TOKEN = Settings.Settings.get_setting_value('telegram_token')

reload(sys)
sys.setdefaultencoding('utf-8')

logger = Logger()


def start(bot, update):
    user_name = update.message.from_user.first_name
    greeting_msg = u'Привет, %s!' \
                   u'Для поиска введите фрагмент или полное название, либо ИНН.' % user_name

    bot.sendMessage(chat_id=update.message.chat_id, text=greeting_msg)


def find_org(bot, update):
    if len(update.message.text) > 255:
        make_no_results_message(bot, update)
    logger.write_info_message(
        'From - ' +
        update.message.from_user.first_name + ' ' + update.message.from_user.last_name +
        ' text - ' + update.message.text
    )
    try:
        bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        org_info_generator = OrgInfoGenerator.OrgInfoGenerator()

        orgs_list = org_info_generator.get_org_list(update.message.text)
        logger.write_info_message('Всего найдено - ' + str(len(orgs_list)))
        if len(orgs_list) < 1:
            make_no_results_message(bot, update)
        if len(orgs_list) >= 1:
            if len(orgs_list) != 1:
                next_org_id = insert_org_list(orgs_list)
                buttons = InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text='Следующий результат', callback_data=str(next_org_id))]]
                )
            else:
                buttons = None

            find_count_info = 'Найдено ' + str(len(orgs_list)) + '\n'
            message = find_count_info + make_org_info_message(orgs_list[0])
            bot.sendMessage(chat_id=update.message.chat_id, text=message, parse_mode='HTML')
            if hasattr(orgs_list[0], 'address'):
                bot.sendLocation(
                    chat_id=update.message.chat_id,
                    latitude=orgs_list[0].address.latitude, longitude=orgs_list[0].address.longitude,
                    reply_markup=buttons
                )
            else:
                message = emojize(':face_screaming_in_fear:',
                                  use_aliases=True) + u'Не найдена информация о местоположении!'
                bot.sendMessage(
                    chat_id=update.message.chat_id,
                    text=message,
                    reply_markup=buttons
                )
        else:
            buttons = None
    except Exception as ex:
        tb = sys.exc_info()[-1]
        stk = traceback.extract_tb(tb, 1)
        function_name = stk[0][2]
        problem_line = stk[0][1]
        logger.write_error_message(
            'Global error in function ' + function_name + '(line: ' + str(problem_line) + '): ' + ex.message)
        message = emojize(':thinking_face:', use_aliases=True) + u'В процессе поиска произошла ошибка!'
        bot.sendMessage(chat_id=update.message.chat_id, text=message, parse_mode='HTML')


def get_other_result(bot, update):
    logger.write_info_message(
        'Callback query: From - ' +
        update.callback_query.message.chat.first_name +
        ' query_id = ' + update.callback_query.data
    )
    bot.sendChatAction(chat_id=update.callback_query.message.chat_id, action=telegram.ChatAction.TYPING)
    current_org, previous_org, next_org = get_org(int(update.callback_query.data))

    message = make_org_info_message(current_org)

    buttons = []
    if previous_org is not None:
        buttons = make_buttons(buttons, 'Предыдущий результат', previous_org.id)
    if next_org is not None:
        buttons = make_buttons(buttons, 'Следующий результат', next_org.id)

    buttons = InlineKeyboardMarkup(buttons)

    bot.sendMessage(chat_id=update.callback_query.message.chat_id, text=message, parse_mode='HTML')
    if current_org.address is not None:
        bot.sendLocation(
            chat_id=update.callback_query.message.chat_id,
            latitude=current_org.address.latitude, longitude=current_org.address.longitude,
            reply_markup=buttons
        )
    else:
        message = emojize(':face_screaming_in_fear:', use_aliases=True) + u'Не найдена информация о местоположении!'
        bot.sendMessage(
            chat_id=update.callback_query.message.chat_id,
            text=message,
            reply_markup=buttons
        )


def make_no_results_message(bot, update):
    message = emojize(':worried_face:', use_aliases=True) + \
              u'К сожалению, но по вашему запросу ничего не найдено.\nПопробуйте еще раз.'
    bot.sendMessage(
        chat_id=update.message.chat_id,
        text=message
    )


def make_buttons(buttons, button_text, call_data):
    button = [
        InlineKeyboardButton(text=button_text, callback_data=str(call_data))
    ]
    buttons.append(button)
    return buttons


def main():
    logger.write_info_message('Bot started.')
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
    except Exception as ex:
        logger.write_error_message('Error occurred! More info: %s' % ex.message)


def exit_handler():
    logger.write_info_message('Bot stopped.')


atexit.register(exit_handler)
if __name__ == '__main__':
    main()
