import requests
import json

from Geo import Geo

BASE_URL = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/%s'


def parse_data(response):
    addresses_info = json.loads(json.dumps(response.json()))
    result = []
    for address_info in addresses_info['suggestions']:
        result.append(Geo(address_info['unrestricted_value'],
                          address_info['data']['geo_lat'],
                          address_info['data']['geo_lon']))

    return result


class AddressInfoGenerator(object):
    """
    Making list of organizations
    """

    def __init__(self, api_token):
        self.api_token = api_token
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
