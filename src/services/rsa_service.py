'''RSA salaus ja purku sekä avainten generointi'''
import random
class RsaService:
    '''salauksen sovelluslogiikasta vastaava luokka'''

    def n_odd_random(self, n_value):
        '''luo random parittoman luvun, parametrina bittikoko'''
        r_value = random.randrange(2**(n_value-1)+1, 2**n_value - 1)
        if r_value % 2 == 0:
            r_value += 1
        return r_value

    def sieve_of_eratosthenes(self, n_value):
        '''luo listan alkuluvuista välillä 2-n'''
        ret = []
        prime = [True for i in range(n_value+1)]
        p_value = 2
        while p_value * p_value <= n_value:
            if prime[p_value] == True:
                for i in range(p_value * p_value, n_value+1, p_value):
                    prime[i] = False
            p_value += 1
        for p_value in range(2, n_value+1):
            if prime[p_value]:
                ret.append(p_value)
        return ret

    def low_level_primality_check(self, candidate):
        '''pikatarkistus, onko luku jaollinen jollain ensimmäisistä alkuluvuista'''
        prime_list = self.sieve_of_eratosthenes(200)
        if candidate in prime_list:
            return True
        is_prime = True
        for prime in prime_list:
            if candidate % prime == 0:
                is_prime = False
        return is_prime

    def miller_rabin_check(self,n_val):
        '''testaa onko annettu luku suurella todennäköisyydellä alkuluku'''
        exp = 0
        a_val = n_val-1
        while a_val % 2 == 0:
            a_val = a_val // 2
            exp += 1
        assert 2**exp * a_val == n_val-1
        m_val = a_val
        a_for_test = random.randrange(2, n_val-1)

        def test_unit(a_for_test):
            '''yksittäinen miller-rabin testi'''
            if pow(a_for_test, m_val, n_val) == 1 or pow(a_for_test, m_val, n_val) == n_val-1:
                return False # a_for_test luultavasti ON alkuluku.
            for i in range(1,exp):
                if pow(a_for_test, 2**i * m_val, n_val) == n_val-1:
                    return False
            return True #  a_for_test varmasti EI ole alkuluku.

        #40 testiä eri a:n arvoilla:
        for i in range(40):
            a_for_test  = random.randrange(2, n_val)
            if test_unit(a_for_test):
                return False
        return True

    def find_low_level_candidate(self, candidate):
        '''etsii seuraavan pikatestin läpäisevän luvun'''
        while not self.low_level_primality_check(candidate):
            candidate += 2
        return candidate

    def create_p(self):
        '''luo alkuluvun p'''
        found = False
        while not found:
            candidate = self.n_odd_random(512)
            low_level_candidate = self.find_low_level_candidate(candidate)
            found = self.miller_rabin_check(low_level_candidate)
            if low_level_candidate % 65537 == 0:
                found = False
        return low_level_candidate

    def create_q(self,p_value):
        '''luo alkuluvun q joka on p:n co-prime'''
        found = False
        while not found:
            candidate = self.n_odd_random(512)
            low_level_candidate = self.find_low_level_candidate(candidate)
            found = self.miller_rabin_check(low_level_candidate)
            if found and low_level_candidate == p_value:
                found = False
            if low_level_candidate % 65537 == 0:
                found = False
        return low_level_candidate

    def create_keys(self):
        '''luo avainparin, julkisen ja yksityisen avaimen'''
        p_value = self.create_p()
        q_value = self.create_q(p_value)
        big_n = p_value * q_value
        r_value = (p_value-1) * (q_value-1)
        e_value = 65537
        d_value = self.extended_eucleidian(e_value, r_value)[0]
        if d_value < 0:
            d_value += r_value

        return (d_value,e_value,big_n)

    def en_crypt(self,e_val,n_val,msg):
        '''suorittaa salauksen'''
        ret = pow(msg,e_val,n_val)
        return ret

    def de_crypt(self,d_val,n_val,msg):
        '''suorittaa purkamisen'''
        ret = pow(msg,d_val,n_val)
        return ret

    def extended_eucleidian(self,a_val,b_val):
        '''tuottaa d-komponentin yksityiseen avaimeen'''
        s_val = 0
        old_s = 1
        r_val = b_val
        old_r = a_val
        while r_val != 0:
            quotient = old_r // r_val
            old_r, r_val =  r_val, old_r - quotient * r_val
            old_s, s_val =  s_val, old_s - quotient * s_val
        if b_val != 0:
            bezout_t = (old_r - old_s * a_val)	 // b_val
        else:
            bezout_t = 0
        return old_s, bezout_t, old_r
        # output "Bézout coefficients:", (old_s, bezout_t)
        # output "greatest common divisor:", old_r
