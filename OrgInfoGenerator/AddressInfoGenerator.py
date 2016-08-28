import requests
import json

import Settings.Settings
from Geo import Geo

BASE_URL = Settings.Settings.get_setting_value('dadata_url')
TOKEN = Settings.Settings.get_setting_value('dadata_token')


def parse_data(response):
    addresses_info = json.loads(json.dumps(response.json()))
    result = []
    for address_info in addresses_info['suggestions']:
        result.append(Geo(address_info))

    return result


class AddressInfoGenerator(object):
    """
    Making list of organizations
    """

    def __init__(self):
        self.api_token = TOKEN
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token %s' % self.api_token
        }

    def get_address_coords(self, search_string):
        url = BASE_URL % 'address'
        body = {
            'query': search_string,
            'count': 1
        }
        response = requests.post(url, headers=self.headers, json=body)
        return parse_data(response)
