import unittest
from services.conversion_service import ConversionService

class TestConversionService(unittest.TestCase):

    def setUp(self):
        self.conversionService = ConversionService()

    def test_char_a_equals_97(self):
        a_bin = self.conversionService.encode_str_to_bin("a")
        self.assertEqual(a_bin, 97)    

    def test_int_97_equals_char_a(self):
        a_str = self.conversionService.encode_bin_to_string(97)
        self.assertEqual(a_str, "a")      
        