# -*- coding: utf-8 -*-
import json

import requests

from Domain import Organization
from Domain import Requisites
from Domain import State
from Domain import Management

import Settings.Settings

BASE_URL = Settings.Settings.get_setting_value('dadata_url')
TOKEN = Settings.Settings.get_setting_value('dadata_token')


def parse_data(response):
    organizations_info = json.loads(json.dumps(response.json()))
    result = []
    for organization_info in organizations_info['suggestions']:
        org_state = State.State(organization_info['data']['state'])

        if organization_info['data']['type'] == 'LEGAL':
            management = Management.Management(organization_info['data']['management'])

            legal_requisites = Requisites.LegalRequisites(
                organization_info['data']['inn'],
                organization_info['data']['ogrn'],
                organization_info['data']['opf']['code'],
                organization_info['data']['kpp']
            )
            organization_element = Organization.LegalOrganization(
                organization_info['unrestricted_value'],
                legal_requisites,
                org_state,
                organization_info['data']['address']['value'],
                management
            )
        elif organization_info['data']['type'] == 'INDIVIDUAL':
            legal_requisites = Requisites.IndividualRequisites(
                organization_info['data']['inn'],
                organization_info['data']['ogrn'],
                organization_info['data']['opf']['code']
            )
            organization_element = Organization.IndividualOrganization(
                organization_info['unrestricted_value'],
                legal_requisites,
                org_state,
                organization_info['data']['address']['value']
            )

        result.append(organization_element)
    return result


class OrgInfoGenerator(object):
    """
    Making list of organizations
    """

    def __init__(self):
        self.api_token = TOKEN
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token %s' % self.api_token
        }

    def get_org_list(self, search_string):
        url = BASE_URL % 'party'
        body = {
            'query': search_string
        }
        response = requests.post(url, headers=self.headers, json=body)
        return parse_data(response)
