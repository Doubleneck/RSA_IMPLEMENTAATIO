import unittest
import random
import string
from services.conversion_service import ConversionService

class TestConversionService(unittest.TestCase):

    def setUp(self):
        self.conversionService = ConversionService()

    def get_random_string(self,length):
        result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))    
        return result_str  

    def test_char_a_equals_97(self):
        a_bin = self.conversionService.encode_str_to_bin("a")
        self.assertEqual(a_bin, 97)

    def test_int_97_equals_char_a(self):
        a_str = self.conversionService.encode_bin_to_string(97)
        self.assertEqual(a_str, "a")

    def test_random_char(self):
        random_string = self.get_random_string(32)
        random_as_bin = self.conversionService.encode_str_to_bin(random_string)
        converted_str = self.conversionService.encode_bin_to_string(random_as_bin)
        self.assertEqual(random_string, converted_str)    
        