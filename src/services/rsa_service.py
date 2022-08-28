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
            if prime[p_value] is True:
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
        '''testaa onko annettu luku suurella todennäköisyydellä alkuluku

        Args:
            n_val (integer): testattava alkuluku.

        Returns:
            True, jos argumenttina annettu luku (todennäköisesti) on alkuluku,
            muussa tapauksessa False.
        '''
        exp = 0
        a_val = n_val-1
        while a_val % 2 == 0:
            a_val = a_val // 2
            exp += 1
        assert 2**exp * a_val == n_val-1
        m_val = a_val
        a_for_test = random.randrange(2, n_val-1)

        def test_unit(a_for_test):
            '''yksittäinen miller-rabin testi, testaa onko luku komposiitti'''
            if pow(a_for_test, m_val, n_val) == 1 or pow(a_for_test, m_val, n_val) == n_val-1:
                return False # a_for_test luultavasti ei ole komposiitti.
            for i in range(1,exp):
                if pow(a_for_test, 2**i * m_val, n_val) == n_val-1:
                    return False # a_for_test luultavasti ei ole komposiitti.
            return True #  a_for_test varmasti on komposiitti.

        #40 testiä eri a:n arvoilla:
        for _ in range(40):
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
        return low_level_candidate

    def create_q(self,p_value):
        '''luo alkuluvun q, niin että phi-totientti (p-1 * q-1) on
            e-komponentin co-prime

        Args:
            p_value(integer): aiemmin generoitu random-alkuluku P.
        Returns:
            q_candidate(integer): alkuluku Q,
            joka toteuttaa ehdon (p-1 * q-1) on e-komponentin co-prime.
        '''
        found = False
        while not found:
            q_candidate = self.create_p()
            found = True
            if q_candidate == p_value:
                found = False
            if (q_candidate - 1 * p_value -1) % 65537 == 0:
                found = False
        return q_candidate

    def create_keys(self):
        '''luo avainparin, julkisen ja yksityisen avaimen'''
        p_value = self.create_p()
        q_value = self.create_q(p_value)
        big_n = p_value * q_value
        r_value = (p_value-1) * (q_value-1)
        e_value = 65537
        d_value = self.extended_eucleidian(e_value, r_value)
        return (d_value,e_value,big_n)

    def en_crypt(self,e_val,n_val,msg):
        '''suorittaa salauksen

        Args:
            e_val(integer):salauseksponentti e = 65537.
            n_val(integer):salauksen modulus N.
            msg(integer):salattava viesti muutettuna kokonaisluvuksi.

        Returns:
            ret(integer):salattu viesti kryptattuna
        '''
        ret = pow(msg,e_val,n_val)
        return ret

    def de_crypt(self,d_val,n_val,msg):
        '''suorittaa purkamisen

        Args:
            d_val(integer):salauseksponentti d.
            n_val(integer):salauksen modulus N.
            msg(integer):salattu viesti muutettuna kokonaisluvuksi.

        Returns:
            ret(integer):purettu viesti kokonaislukuna.
        '''
        ret = pow(msg,d_val,n_val)
        return ret

    def extended_eucleidian(self,a_val,b_val):
        '''tuottaa d-komponentin yksityiseen avaimeen

        Args:
            a_val(integer):ensimmäinen testattava kokonaisluku, tässä saa
            arvokseen salauseksponetin e.
            b_val(integer):toinen testattava kokonaisluku, tässä saa arvokseen
            phi-totientin (q-1)*(p-1)

        Returns:
           old_s(integer): Bézout coefficient, joka on tässä myös d-komponetti.

        '''
        if a_val > b_val:
            a_val, b_val = b_val, a_val
        s_val = 0
        old_s = 1
        r_val = b_val
        old_r = a_val
        while r_val != 0:
            quotient = old_r // r_val
            old_r, r_val =  r_val, old_r - quotient * r_val
            old_s, s_val =  s_val, old_s - quotient * s_val
        if old_s < 0:
            old_s += b_val
        return old_s
