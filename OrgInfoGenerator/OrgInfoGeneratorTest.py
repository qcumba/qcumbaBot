# -*- coding: utf-8 -*-
import unittest

from OrgInfoGenerator import OrgInfoGenerator


class MyTestCase(unittest.TestCase):

    def test_count(self):
        search_string = 'Сбербанк'
        org_info_generator = OrgInfoGenerator()
        result = org_info_generator.get_org_list(search_string)
        count = len(result)
        self.assertTrue(count > 0, 'Количество найденного = ' + str(count))

if __name__ == '__main__':
    unittest.main()
