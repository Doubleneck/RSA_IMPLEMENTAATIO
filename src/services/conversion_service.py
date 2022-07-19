'''teksti-binääri konversio'''
class ConversionService:
    '''konversiosta vastaava luokka'''
    def encode_str_to_bin(self, string):
        '''muuntaa merkkijonon binääriksi'''
        char_bits = 8
        b_t = 0
        for char in string:
            b_t <<= char_bits
            b_t |= ord(char)
        return b_t

    def encode_bin_to_string(self, b_t):
        '''muuntaa binäärin merkkijonoksi'''
        char_bits = 8
        bit_mask = 2**char_bits-1
        out = ""
        while b_t != 0:
            out = chr(b_t & bit_mask) + out
            b_t >>= char_bits
        return out
        