from services.rsa_service import RsaService
#from services import ConversionService

class UI:
    def __init__(self):
        pass
    
    def start():
        print("***RSA-GENERAATTORI JA KOODERI/DEKOODERI*** \n")
        #print("1 -  \n")
        #print("lopeta valitsemalla q ja Enter \n")

        while True:
            select = input("Valitse toiminto: \n 1 - avainten generointi \n 2 - salaaminen \n 3 - purkaminen\n q - lopetus \n " )
            print("\n")
            if select == "q":
                quit()
            if select not in ["1","2","3","q"]:
                print("Väärä valinta...yritä uudelleen \n")
            if select == "1":
                print("GENEROIDAAN / DEMO \n")   
            if select == "2":
                print("SALATAAN / DEMO \n")    
            if select == "3":
                print("PURETAAN / DEMO \n") 
