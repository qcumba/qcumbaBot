# -*- coding: utf-8 -*-

import unittest

from AddressInfoGenerator import AddressInfoGenerator


class MyTestCase(unittest.TestCase):
    dadata_token = '962ece1f054b4f80f558b93fd4fa635692530c48'

    def test_count(self):
        search_string = '117312, г Москва, ул Вавилова, д 19'
        org_info_generator = AddressInfoGenerator(self.dadata_token)
        result = org_info_generator.get_address_coords(search_string)
        count = len(result)
        self.assertTrue(count == 1)


if __name__ == '__main__':
    unittest.main()
