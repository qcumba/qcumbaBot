# -*- coding: utf-8 -*-
import datetime


class State(object):
    """
    Current state of the organization
    """

    def __init__(self, status):
        state = status['status']
        if state == 'ACTIVE':
            self.status = 'Действующая'

        if state == 'LIQUIDATED':
            self.status = 'Ликвидирована'
            self.liquidation_date = datetime.datetime.fromtimestamp(float(status['liquidation_date']) / 1000).strftime('%d.%m.%Y')
        else:
            self.liquidation_date = None

        self.registration_date = datetime.datetime.fromtimestamp(float(status['registration_date']) / 1000).strftime('%d.%m.%Y')
