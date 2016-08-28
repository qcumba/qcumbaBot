# -*- coding: utf-8 -*-
import requests
import json

import Organization
import Requisites
import Settings.Settings
from State import State

BASE_URL = Settings.Settings.get_setting_value('dadata_url')
TOKEN = Settings.Settings.get_setting_value('dadata_token')


def parse_data(response):
    organizations_info = json.loads(json.dumps(response.json()))
    result = []
    for organization_info in organizations_info['suggestions']:
        org_state = State(organization_info['data']['state'])

        if organization_info['data']['type'] == 'LEGAL':
            management = Requisites.Management(organization_info['data']['management'])

            legal_requisites = Requisites.LegalRequisites(organization_info['data']['inn'],
                                                          organization_info['data']['ogrn'],
                                                          organization_info['data']['opf']['code'],
                                                          organization_info['data']['kpp'],
                                                          management)
            organization_element = Organization.LegalOrganization(organization_info['unrestricted_value'],
                                                                  legal_requisites,
                                                                  org_state,
                                                                  organization_info['data']['address']['value'])
        elif organization_info['data']['type'] == 'INDIVIDUAL':
            legal_requisites = Requisites.IndividualRequisites(organization_info['data']['inn'],
                                                               organization_info['data']['ogrn'],
                                                               organization_info['data']['opf']['code'])
            organization_element = Organization.IndividualOrganization(organization_info['unrestricted_value'],
                                                                       legal_requisites,
                                                                       org_state,
                                                                       organization_info['data']['address']['value'])

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
