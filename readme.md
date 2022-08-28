# Tietorakenteiden ja algoritmien harjoitustyö:RSA-salaus

Sovellus on 1024bit RSA-avaingeneraattori ja encoder/decoder tekstikäyttöliittymällä. Harjoitustyö on tehty Helsingin Yliopiston TKT:n kandiohjelman kurssilla "Tietorakenteiden ja algoritmien harjoitustyö" (loppukesä 2022).
 
##  Python-versio:

Sovelluksen toiminta on testattu Python-versiolla `3.8` Mac OS ja Ubuntu Linux käyttöjärjestelmissä.

## Dokumentaatio

- [käyttöohje](https://github.com/Doubleneck/RSA_IMPLEMENTAATIO/blob/master/dokumentaatio/kayttoohje.md)  
- [vaatimusmäärittely](https://github.com/Doubleneck/RSA_IMPLEMENTAATIO/blob/master/dokumentaatio/vaatimusmaarittely.md)  
- [testausdokumentti](https://github.com/Doubleneck/RSA_IMPLEMENTAATIO/blob/master/dokumentaatio/testausdokumentti.md)  
- [toteutusdokumentti](https://github.com/Doubleneck/RSA_IMPLEMENTAATIO/blob/master/dokumentaatio/toteutusdokumentti.md)  


### Viikkoraportit
- [Viikko 1](./dokumentaatio/Viikkoraportti1.md)<br>
- [Viikko 2](./dokumentaatio/Viikkoraportti2.md)<br>
- [Viikko 3](./dokumentaatio/Viikkoraportti3.md)<br>
- [Viikko 4](./dokumentaatio/Viikkoraportti4.md)<br>
- [Viikko 5](./dokumentaatio/Viikkoraportti5.md)<br>
- [Viikko 6](./dokumentaatio/Viikkoraportti6.md)<br>
- [Viikko 7](./dokumentaatio/Viikkoraportti7.md)<br>

## Asennus

1. Asenna riippuvuudet:
```bash
poetry install
```
Jos komentoa poetry ei löydy, saatat tarvita ensin komennon:
```bash
 source $HOME/.poetry/env
```

2. Siirry virtuaaliympäristöön komennolla:
```bash
poetry shell
```

3. Sovelluksen käynnistys
```bash
poetry run invoke start
```
### Testaus

Yksikkötestaus suoritetaan virtuaaliympäristössä komennolla:
```bash
poetry run invoke test
```

Manuaalinen integraatiotestaus suoritetaan virtuaaliympäristössä komennolla:
```bash
poetry run invoke manual-test
```
(huom, manuaalitesti kestää useita minuutteja)

### Testikattavuus

Yksikkötestien Testikattavuusraportin voi generoida komennolla:
```bash
poetry run invoke coverage-report 
```
Raportti generoituu _htmlcov_-hakemistoon.



### Pylint

Koodin tyylitarkistuksen voit tehdä komennolla:
```bash
poetry run invoke lint 
```
Lintteri tarkistaa kansion src tiedostot, poislukien index.py, tests-kansion tiedostot sekä käyttöliittymäkansion ui tiedostot.

