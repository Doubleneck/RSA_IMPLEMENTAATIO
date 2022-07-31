from tarfile import SYMTYPE
import unittest
import sympy
from random import randint
from services.rsa_service import RsaService

class TestRsaService(unittest.TestCase):

    def setUp(self):
        self.rsaService = RsaService()

    def test_n_odd_random_creates_odd(self):
        '''testaa, että luotu 512-bittinen random on pariton'''
        a_bin = self.rsaService.n_odd_random(512)
        self.assertEqual(False, a_bin % 2 == 0)

    def test_sieve_of_eratosthenes_200(self):
        '''testaa, että 200 ensimmäisen alkuluvun generointi toimii oikein'''
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
    
    def test_create_p_test_is_prime(self):
        '''testaa onko luotu p alkuluku'''
        prime_candidate = self.rsaService.create_p()
        self.assertEqual(True, sympy.isprime(prime_candidate))

    def test_create_p_test_is_random(self):
        '''testaa ovatko 2 luotua lukua p  eri luvut'''
        prime_candidate = self.rsaService.create_p()
        prime_candidate2 = self.rsaService.create_p()
        self.assertEqual(False, prime_candidate == prime_candidate2)    

    def test_create_q_test_is_prime(self):
        '''testaa onko luotu q alkuluku'''
        prime_p = self.rsaService.create_p()
        q_prime_candidate = self.rsaService.create_q(prime_p)
        self.assertEqual(True, sympy.isprime(q_prime_candidate))


    def test_create_q_test_totient_is_co_prime_with_e(self):
        '''testaa 10 x onko luotujen alkulukujen p ja q avulla muodostettu totientti e:n coprime'''
        i = 0
        e_value = 65537
        ret = True
        while i < 10:
            prime_p = self.rsaService.create_p()
            prime_q = self.rsaService.create_q(prime_p)
            ret = (prime_p-1) * (prime_q-1) % e_value != 0
            if not ret:
                break
            i += 1    
        self.assertEqual(True, ret)

    def test_find_low_level_candidate(self):
        self.assertEqual(191,self.rsaService.find_low_level_candidate(183))

    def test_miller_rabin_is_not_prime_big(self):
        '''testaa miller-rabinia viidellä luvulla joka on komposiitti'''
        i = 0
        while i < 5:        
            a = sympy.randprime(pow(2,511), pow(2,512))
            b = sympy.randprime(pow(2,511), pow(2,512))
            test_passed = self.rsaService.miller_rabin_check(a*b)
            if test_passed:
                break
            i += 1
        self.assertNotEqual(True, test_passed)

    def test_miller_rabin_is_prime_big(self):
        '''testaa miller-rabinia viidellä 512 bit random -alkuluvulla'''
        i = 0
        while i < 5:
            a = sympy.randprime(pow(2,511), pow(2,512))
            test_passed = self.rsaService.miller_rabin_check(a)
            if not test_passed:
                break
            i += 1
        self.assertEqual(True, test_passed)

    def test_extended_eucleidian(self):
        '''testaa että algoritmi palauttaa toimivan d-komponentin'''
        a_value = sympy.randprime(pow(2,511), pow(2,512))
        b_value = sympy.randprime(pow(2,511), pow(2,512))
        totient = (a_value-1) * (b_value-1)
        e_value = 65537
        d_value = self.rsaService.extended_eucleidian(e_value,totient)   
        self.assertEqual(1, e_value * d_value % totient) 

    def test_extended_eucleidian(self):
        '''testaa että algoritmi palauttaa toimivan d-komponentin, jos arvot annettu a>b'''
        a_value = sympy.randprime(pow(2,511), pow(2,512))
        b_value = sympy.randprime(pow(2,511), pow(2,512))
        totient = (a_value-1) * (b_value-1)
        e_value = 65537
        d_value = self.rsaService.extended_eucleidian(totient,e_value)   
        self.assertEqual(1, e_value * d_value % totient)     

    def test_encrypt_decrypt_random_int(self):
        '''testaa salauksen ja purun 512-bittisellä luvulla'''
        random_integer = randint(pow(2,511),pow(2,512))
        keys = self.rsaService.create_keys()
        cipher_integer = self.rsaService.en_crypt(keys[1],keys[2],random_integer)
        plain_integer = self.rsaService.de_crypt(keys[0],keys[2],cipher_integer)
        self.assertEqual(random_integer, plain_integer)

    def test_encrypt_decrypt_random_int(self):
        '''testaa salauksen ja purun epäonnistumisen väärällä avaimella'''
        random_integer = randint(pow(2,511),pow(2,512))
        keys = self.rsaService.create_keys()
        wrong_keys = self.rsaService.create_keys()
        cipher_integer = self.rsaService.en_crypt(keys[1],keys[2],random_integer)
        plain_integer = self.rsaService.de_crypt(wrong_keys[0],keys[2],cipher_integer)
        self.assertNotEqual(random_integer, plain_integer)    

    def test_key_generator_generates_tuple_of_3(self):
        keys = self.rsaService.create_keys()
        self.assertEqual(3, len(keys))

    def test_key_generator_e_component_is_right(self):
        keys = self.rsaService.create_keys()
        self.assertEqual(65537, keys[1])    
