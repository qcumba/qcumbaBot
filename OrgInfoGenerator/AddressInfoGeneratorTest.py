# -*- coding: utf-8 -*-

import unittest
import Settings.Settings

from AddressInfoGenerator import AddressInfoGenerator


class MyTestCase(unittest.TestCase):
    dadata_token = Settings.Settings.get_setting_value('dadata_token')

    def test_count(self):
        search_string = '117312, г Москва, ул Вавилова, д 19'
        org_info_generator = AddressInfoGenerator(self.dadata_token)
        result = org_info_generator.get_address_coords(search_string)
        count = len(result)
        self.assertTrue(count == 1)


if __name__ == '__main__':
    unittest.main()
