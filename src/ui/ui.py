from services.conversion_service import ConversionService
from services.rsa_service import RsaService

class UI:
    def __init__(self):
        pass

    def start():
        print("***RSA-GENERAATTORI JA KOODERI/DEKOODERI*** \n")

        while True:
            select = input("Valitse toiminto: \n 1 - avainten generointi \n 2 - salaaminen \n 3 - purkaminen\n q - lopetus \n " )
            print("\n")
            if select == "q":
                quit()
            if select not in ["1","2","3","q"]:
                print("Väärä valinta...yritä uudelleen \n")
            if select == "1":
                print("GENEROIDAAN / DEMO (=GENEROIDAAN P!) \n")   
                P = RsaService().create_p()
                print(P)
            if select == "2":
                print("SALATAAN / DEMO (= NYT MUUNTAA) \n")   
                while True:
                    pubKey = input("Anna julkinen avain: \n")
                    message = input("Kirjoita viesti: \n")
                    nro = ConversionService().encode_str_to_bin(message)
                    print("viesti numerona on: ", nro)
                    print("numero viestinä on: ", ConversionService().encode_bin_to_string(nro))
                    rr = 5
                    P = RsaService().sieve_of_eratosthenes(200)
                  #  Q = RsaService.n_odd_random(10)
                    #S = RsaService.low_level_primality_check(self,211)
                    R = RsaService().low_level_primality_check(211)
                    
                    #N = P * Q
                    print(P)
                    print(R)
                   # print(Q)
                  #  print(S)
                    
                    break
                    

            if select == "3":
                print("PURETAAN / DEMO \n") 
