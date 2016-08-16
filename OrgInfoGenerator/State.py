# -*- coding: utf-8 -*-
import datetime


class State(object):
    """
    Current state of the organization
    """

    def __init__(self, status, registration_date, actuality_date):
        if status == 'ACTIVE':
            self.status = 'Действующая'
        if status == 'LIQUIDATED':
            self.status = 'Ликвидирована'

        reg_date = datetime.datetime.fromtimestamp(float(registration_date) / 1000).strftime('%d.%m.%Y')
        act_date = datetime.datetime.fromtimestamp(float(actuality_date) / 1000).strftime('%d.%m.%Y')

        self.registration_date = reg_date
        self.actuality_date = act_date
