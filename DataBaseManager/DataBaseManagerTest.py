# import unittest
# import TestHelpers
# from DataBaseManager import insert_org_list
#
#
# class MyTestCase(unittest.TestCase):
#     def simple_insert(self):
#         i = 0
#         orgs_list = []
#         while i < 10:
#             orgs_list.append(TestHelpers.generate_random_org())
#             i += 1
#         insert_org_list(orgs_list)
#
#         self.assertTrue(True)
#
# if __name__ == '__main__':
#     unittest.main()
#
#
# -*- coding: utf-8 -*-

import unittest
import TestHelpers
from DataBaseManager import insert_org_list


class MyTestCase(unittest.TestCase):

    def test_count(self):
        i = 0
        orgs_list = []
        while i < 10:
            orgs_list.append(TestHelpers.generate_random_org())
            i += 1
        insert_org_list(orgs_list)
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()