
class RsaService:
    '''RSA salauksen sovelluslogiikasta vastaava luokka'''

    def __init__(self):
        pass

    def encodeStrToBin(string):
        charBits = 8
        b = 0
        for c in string:
            b <<= charBits
            b |= ord(c)
        return b

    def encodeBinToString(b):
        charBits = 8
        bitMask = 2**charBits-1
        out = ""
        while b != 0:
            out = chr(b & bitMask) + out
            b >>= charBits
        return out   
