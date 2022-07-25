from tarfile import SYMTYPE
import unittest
import sympy
from services.rsa_service import RsaService

class TestRsaService(unittest.TestCase):

    def setUp(self):
        self.rsaService = RsaService()

    def test_n_odd_random_creates_odd(self):
        a_bin = self.rsaService.n_odd_random(512)
        self.assertEqual(False, a_bin % 2 == 0)

    def test_sieve_of_eratosthenes_200(self):
        prime_list =  self.rsaService.sieve_of_eratosthenes(200)
        control_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
        167, 173, 179, 181, 191, 193, 197, 199]
        self.assertEqual(prime_list, control_list)

    def test_low_level_primality_check_small(self):
        self.assertEqual(True, self.rsaService.low_level_primality_check(181))

    def test_low_level_primality_check_small_no_prime(self):
        self.assertEqual(False, self.rsaService.low_level_primality_check(125))

    def test_low_level_primality_check_medium(self):
        self.assertEqual(True, self.rsaService.low_level_primality_check(391939))

    def test_low_level_primality_check_medium_no_prime(self):
        self.assertEqual(False, self.rsaService.low_level_primality_check(400000000))

    def test_low_level_primality_check_big(self):
        self.assertEqual(True, self.rsaService.low_level_primality_check(10969764891642967028739597576355893629690708119113625579670998564945570092957573289791980389514640480614111598007397242657731590795479703780703838025508199))

    def test_low_level_primality_check_big_no_prime(self):
        self.assertEqual(False, self.rsaService.low_level_primality_check(10969764891642967028739597576355893629690708119113625579670998564945570092957573289791980389514640480614111598007397242657731590795479703780703838025508200))
    
    def test_miller_rabin_is_not_prime_big(self):
        '''testaa luvulla joka on komposiitti'''
        a = sympy.randprime(pow(2,511), pow(2,512))
        b = sympy.randprime(pow(2,511), pow(2,512))
        self.assertEqual(False, self.rsaService.miller_rabin_check(a*b))

    def test_miller_rabin_is_prime_big(self):
        '''testaa viidellä 512 bit random -alkuluvulla'''
        i = 0
        while i < 4:
            a = sympy.randprime(pow(2,511), pow(2,512))
            test_passed = self.rsaService.miller_rabin_check(a)
            if not test_passed:
                break
            i += 1
        self.assertEqual(True, test_passed)

    def test_extended_eucleidian(self):
        '''testaa että algoritmi palauttaa toimivan d_komponentin'''
        a_value = sympy.randprime(pow(2,511), pow(2,512))
        b_value = sympy.randprime(pow(2,511), pow(2,512))
        totient = (a_value-1) * (b_value-1)
        e_value = 65537
        d_value = self.rsaService.extended_eucleidian(e_value,totient)   
        self.assertEqual(1, e_value * d_value % totient) 
