# -*- coding: utf-8 -*-
import unittest
import second
import os

class Check(unittest.TestCase):

	def test_file_exist(self):
		self.assertTrue(os.path.isfile(second.file))

	def test_cases_is_int(self):
		for block in second.records:
			self.assertTrue(block['cases'].isdigit())

	def test_countryArray(self):
		self.assertNotEqual(len(second.countryArray), 0)
