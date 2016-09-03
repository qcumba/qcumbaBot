# -*- coding: utf-8 -*-
import logging

import datetime


def make_name_by_date():
    now_date = datetime.date.today().strftime('%d.%m.%Y')
    name = 'logs/log_' + now_date + '.log'
    return name


class Logger(object):
    """
    Provides a set of of convenience functions for logging usage
    """

    logging_level = logging.INFO
    file_name = make_name_by_date()
    logging_format = '%(asctime)s - %(levelname)s - %(message)s'

    def __init__(self):
        # logging only warning messages from requests
        logging.getLogger("requests").setLevel(logging.WARNING)
        logging.basicConfig(
            level=self.logging_level,
            filename=self.file_name,
            format=self.logging_format
        )

    def write_info_message(self, message):
        logging.info(message)

    def write_error_message(self, message):
        logging.error(message)