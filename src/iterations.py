'''integraatiotestimoduli'''
import random
import string
from services.conversion_service import ConversionService
from services.rsa_service import RsaService

def get_random_string(length):
    '''generoi random stringin, jossa sekalaisia ascii merkkejä'''
    characters = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join(random.choice(characters) for i in range(length))
    return result_str

def main():
    '''testaa n (=iterations) kertaa salausoperaation edestakaisin
       avainparin generoimiseen. Lisäksi ilmoittaa, jos peräkkäin tulee sama avainpari'''
    iterations = 1000
    ret = False
    old_keys = None
    same_key = 0
    for i in range (iterations):
        message = str(get_random_string(32))
        msg_bin = ConversionService().encode_str_to_bin(message)
        rsa_keys = RsaService().create_keys()
        d_value = rsa_keys[0]
        e_value = rsa_keys[1]
        n_value = rsa_keys[2]
        encrypted_msg = RsaService().en_crypt(e_value, n_value, msg_bin)
        decrypted_msg = RsaService().de_crypt(d_value, n_value, int(encrypted_msg))
        msg_str = ConversionService().encode_bin_to_string(decrypted_msg)
        if old_keys == rsa_keys:
            same_key += 1
        old_keys = rsa_keys
        ret = (message == msg_str)
        if not ret:
            print("Testi ei mennyt läpi kohdassa ",i)
            break
        i += 1

    if ret:
        print("\nTesti meni läpi, salattiin ja purettiin " + str(iterations) + " kertaa")
        print("Sama avain toistui peräkkäin " + str(same_key) + " kertaa\n")

if __name__ == '__main__':
    main()
