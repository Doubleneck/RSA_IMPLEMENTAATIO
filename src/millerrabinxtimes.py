'''testiluokka miller-rabinin laajemmalle testille'''
import sympy
from services.rsa_service import RsaService

def main():
    '''testaa miller-rabinia n kertaa 1024 bit random -komposiitilla ja
    512 bit random-alkuluvulla'''
    print("*" * 40)
    n_value = 100

    test_passed = True
    for _ in range (n_value):
        a_value = sympy.randprime(pow(2,511), pow(2,512))
        b_value = sympy.randprime(pow(2,511), pow(2,512))
        if RsaService().miller_rabin_check(a_value * b_value) is True:
            print("Miller-rabin teki virheen komposiitissa syötteellä: \n", a_value * b_value)
            test_passed = False
            break
    if test_passed:
        print("Oikean tulos komposiiteilla joka kerta.Testattiin ",n_value,"kertaa\n")

    test_passed = True
    for _ in range (n_value):
        a_value = sympy.randprime(pow(2,511), pow(2,512))
        if RsaService().miller_rabin_check(a_value) is False:
            print("Miller-rabin teki virheen alkuluvussa syötteellä: \n", a_value)
            test_passed = False
            break
    if test_passed:
        print("Oikea tulos alkuluvuilla joka kerta. Testattiin ",n_value,"kertaa")

if __name__ == '__main__':
    main()
