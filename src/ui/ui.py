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
              #  print("GENEROIDAAN / DEMO ) \n")   
                rsa_keys = RsaService().create_keys()
                pub_key = str(rsa_keys[1])+"-"+str(rsa_keys[2])
                pri_key = str(rsa_keys[0])+"-"+str(rsa_keys[2])
                print("PUBLIC KEY (e,N): \n")
                print(pub_key,"\n")
                print("******************************************************************************")
                print("PRIVATE KEY (d,N): \n")
                print(pri_key,"\n")

            if select == "2":
              #  print("SALATAAN / DEMO \n")   
                while True:
                    pub_key = input("Anna julkinen avain: \n")
                    e_value = int(pub_key.split("-")[0])
                    n_value = int(pub_key.split("-")[1])
                    message = input("Kirjoita viesti: \n")
                    msg_bin = ConversionService().encode_str_to_bin(message)
                    if msg_bin.bit_length() > 1022:
                        print("viesti on liian pitkä salattavaksi! \n")
                        print(msg_bin.bit_length())
                        break
                    encrypted_msg = RsaService().en_crypt(e_value, n_value, msg_bin)
                    print("**********************************************\n")
                    print("viesti salattuna:\n")
                    print(encrypted_msg)
                    
                    break

            if select == "3":
                while True:
                    pri_key = input("Anna yksityinen avain: \n")
                    d_value = int(pri_key.split("-")[0])
                    n_value = int(pri_key.split("-")[1])
                    crypted_message = input("Anna salattu viesti: \n")
                    decrypted_msg = RsaService().de_crypt(d_value, n_value, int(crypted_message))
                    msg_str = ConversionService().encode_bin_to_string(decrypted_msg)
                    print("**********************************************\n")
                    print("viesti purettuna:\n")
                    print(msg_str)
                    print("**********************************************\n")
                    
                    break 
