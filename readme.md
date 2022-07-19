# Tietorakenteiden ja algoritmien harjoitustyö:RSA-salaus

Sovellus on 1024bit RSA-avaingeneraattori ja encoder/decoder tekstikäyttöliittymällä. 
 
##  Python-versio:

Sovelluksen toiminta on testattu Python-versiolla `3.8`.

## Dokumentaatio

- [käyttöohje](puuttuu)  
- [vaatimusmäärittely](https://github.com/Doubleneck/RSA_IMPLEMENTAATIO/blob/master/dokumentaatio/vaatimusmaarittely.md)  
- [tuntikirjanpito](https://github.com/Doubleneck/RSA_IMPLEMENTAATIO/blob/master/dokumentaatio/tuntikirjanpito.md)
- [testausdokumentti](puuttuu)

## Asennus

1. Asenna riippuvuudet:
```bash
poetry install
```
Jos komentoa poetry ei löydy, saatat tarvita ensin komennon:
```bash
 source $HOME/.poetry/env
 ```
```
2. Sovelluksen käynnistys
```bash
poetry run invoke start
```
### Testaus

Testaus suoritetaan virtuaaliympäristössä komennolla:
```bash
poetry run invoke test
```
### Testikattavuus

Testikattavuusraportin voi generoida komennolla:
```bash
poetry run invoke coverage-report (EI VIELÄ OLEMASSA)
```
Raportti generoituu _htmlcov_-hakemistoon.
