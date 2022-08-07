
## Viimeisin testiraportti, yksikkötestien kattavuus 98% (7.8.):

- [testikattavuus](https://github.com/Doubleneck/RSA_IMPLEMENTAATIO/blob/master/dokumentaatio/kuvat/testikattavuusraportti) 

# Testaus

Olennaisimmat testit liittyvät alkulukujen luontiin ja mm. Miller-Rabin -tarkistuksen testaukseen sekä d-komponentin tuottamiseen vaadittavaan (inverse) euklideen algoritmiin. Yksikkötesteissä on hyödynnetty Pythonin SYMPY-kirjastoa, josta löytyy mm. funktio isPrime(),

## Automaattiset yksikkötestit (RSA-luokka):
Alkulukujen generointi 
  1. Testataan, että luotu alkuluku P on prime (SYMPY isPrime())
  2. Testataan, että alkulukujen luonti tuottaa random-alkulukuja (tarkistetaan kahden generoidun alkuluvun ero)
  3. Testataan, että luotu alkuluku Q on prime (SYMPY isPrime())
  4. Testataan, että luotu alkuluku Q on sellainen, että totientti (p-1) * (q-1) on e:n (=65537) co-prime
  5. Testataan, että Miller Rabin ei erehdy komposiiteissa (testataan komposiitilla, joka on luotu kahden 512bit SYMPY.randprime() luvun tulosta).
  6. Testataan, että Miller Rabin ei erehdy alkuluvussa (testataan alkuluvulla, joka on luotu SYMPY.randprime() -funktiolla).
  
d-komponentin generointi
  1. Testataan, että euklideen algoritmi tuottaa oikeanlaisen d-komponentin, jolle pätee:

      ed = 1 MOD (N)

  2. Testataan, että euklideen algoritmin argumentit voivat olla kummin päin vaan (siltä varalta, että ohjelman rakenne muuttuu(


## Automaattiset yksikkötestit (string/bin konversio-luokka):
String-binääri -konversioitten testaaminen on hyvin suoraviivaista. Testataan, että random string convertoituu binääriksi ja siitä takaisin oikein.


## Manuaaliset testit (RSA-luokka):
Alkulukujen generoinnin testit 5 ja 6 (Miller Rabin alkuluvulla ja komposiitilla) toistettiin kumpikin 10.000 kertaa.

## Manuaalinen integraatiotesti:
Testataan 1000x koko salausproseduuri läpi, eli
  1.Luodaan avaimet
  2.tuotetaan randomviesti
  3.muunnetaan randomviesti binääriksi ja salataan
  4.puretaan salattu viesti ja palautetaan stringiksi
  5.verrataan alkuperäiseen randomviestiin

Lisäksi jokaisella kierrokella verrataan, onko generoitu avain eri kuin edellisellä kierroksella  

  
  
