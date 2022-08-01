
## Viimeisin testiraportti, yksikkötestien kattavuus 98% (31.7.):

- [testikattavuus](https://github.com/Doubleneck/RSA_IMPLEMENTAATIO/blob/master/dokumentaatio/kuvat/testikattavuusraportti_31_7_2022b.png) 

# Testaus

Olennaisimmat testit liittyvät alkulukujen luontiin ja mm. Miller-Rabin -tarkistuksen testaukseen sekä d-komponentin tuottamiseen vaadittavaan (inverse) euklideen algoritmiin. Yksikkötesteissä on hyödynnetty Pythonin SYMPY-kirjastoa, josta löytyy mm. funktio isPrime(),

##Automaattiset yksikkötestit:
- Alkulukujen generointi 
  1. Testataan, että luotu alkuluku P on prime (SYMPY isPrime())
  2. Testataan, että alkulukujen luonti tuottaa random-alkulukuja (tarkistetaan kahden generoidun alkuluvun ero)
  3. Testataan, että luotu alkuluku Q on prime (SYMPY isPrime())
  4. Testataan, että luotu alkuluku Q on sellainen, että totientti (p-1) * (q-1) on e:n (=65537) co-prime
  5. Testataan 5x, että Miller Rabin ei erehdy komposiiteissa (testataan komposiitilla, joka on luotu kahden 512bit SYMPY.randprime() luvun tulosta).
  6. Testataan 5x, että Miller Rabin ei erehdy alkuluvussa (testataan alkuluvulla, joka on luotu SYMPY.randprime() -funktiolla).

  
  
Yksikkötestauksen kattavuusraportti.
Mitä on testattu, miten tämä tehtiin?
Minkälaisilla syötteillä testaus tehtiin (vertailupainotteisissa töissä tärkeää)?
Miten testit voidaan toistaa?
Ohjelman toiminnan empiirisen testauksen tulosten esittäminen graafisessa muodossa.
