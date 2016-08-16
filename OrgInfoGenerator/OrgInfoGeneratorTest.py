# -*- coding: utf-8 -*-

import unittest

from OrgInfoGenerator import OrgInfoGenerator


class MyTestCase(unittest.TestCase):

    dadata_token = '962ece1f054b4f80f558b93fd4fa635692530c48'

    def test_count(self):
        search_string = 'Сбербанк'
        org_info_generator = OrgInfoGenerator(self.dadata_token)
        result = org_info_generator.get_org_list(search_string)
        count = len(result)
        self.assertTrue(count > 0, 'Количество найденного = ' + str(count))

if __name__ == '__main__':
    unittest.main()
