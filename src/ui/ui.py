from services.conversion_service import ConversionService

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
                print("SALATAAN / DEMO (= NYT MUUNTAA) \n")   
                while True:
                    pubKey = input("Anna julkinen avain: \n")
                    message = input("Kirjoita viesti: \n")
                    nro = ConversionService.encodeStrToBin(message)
                    print("viesti numerona on: ", nro)
                    print("numero viestinä on: ", ConversionService.encodeBinToString(nro))
                    break



            if select == "3":
                print("PURETAAN / DEMO \n") 
