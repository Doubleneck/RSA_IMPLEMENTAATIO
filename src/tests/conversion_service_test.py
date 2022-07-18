import unittest
from services.conversion_service import ConversionService

class TestConversionService(unittest.TestCase):

    def setUp(self):
        self.conversionService = ConversionService

    def test_char_a_equals_97(self):
        a_bin = self.conversionService.encodeStrToBin("a")
        self.assertEqual(a_bin, 97)    

    def test_int_97_equals_char_a(self):
        a_str = self.conversionService.encodeBinToString(97)
        self.assertEqual(a_str, "a")      
        