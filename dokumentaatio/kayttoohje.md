# Käyttöohje

## Asennus

1. Asenna riippuvuudet:
```bash
poetry install
```
Jos komentoa poetry ei löydy, saatat tarvita ensin komennon:
```bash
 source $HOME/.poetry/env
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
poetry run invoke coverage-report 
```
Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Koodin tyylitarkistuksen voit tehdä komennolla:
```bash
poetry run invoke lint 
```

## Käyttö

1. Avainten generointi

```bash
 Valitse päävalikosta: 1 - avainten generointi 
```
Ohjelma tulostaa terminaaliin avainparin PUBLIC KEY (e,N) ja PRIVATE KEY (d,N).
Kopioi avaimet salaamista/purkamista varten johonkin tekstityökaluun, esim muistilapulle.


2. Viestin salaus
```bash
Valitse päävalikosta: 2 - salaaminen 
```



