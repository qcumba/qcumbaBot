# -*- coding: utf-8 -*-

import unittest
import Settings.Settings

from AddressInfoGenerator import AddressInfoGenerator


class MyTestCase(unittest.TestCase):

    def test_count(self):
        search_string = '117312, г Москва, ул Вавилова, д 19'
        org_info_generator = AddressInfoGenerator()
        result = org_info_generator.get_address_coords(search_string)
        count = len(result)
        self.assertTrue(count == 1)


if __name__ == '__main__':
    unittest.main()
