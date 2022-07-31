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

Huom! Antaessasi avainta terminaalissa jätä otsikko esim. "PUBLIC KEY (e,N)" pois. 
Avain on muotoa numero1-numero2 väliviivalla erotettuna, missä numero1 on salauskomponentti ja numero2 avainten yhteinen modulus N.

2. Viestin salaus
```bash
Valitse päävalikosta: 2 - salaaminen 
```
Ohjelma kysyy seuraavana salaamiseen käytettävän julkisen avaimen PUBLIC KEY (e,N)

```bash
Pastea kopioimasi julkinen salausavain PUBLIC KEY (e,N) terminaaliin.
```
Ohjelma kysyy seuraavana salattavan viestin

```bash
Kirjoita salattava viesti.
```

(viestin maksimikoko rajoittuu 1024-bit RSA-salauksessa moduluksen kokoon, elu tuohon 1024 bittiin eli Ascii merkistössä 127 merkkiin.
Jos viestissä on asciin ulkopuolisia merkkejä, esim ääkkösiä, maksimiviestin pituus kuitenkin lyhenee.
Ohjelma tulostaa terminaaliin salatun viestin, kopioi se jonnekin.

3. Viestin purkaminen
```bash
Valitse päävalikosta: 3 - purkaminen 
```
Ohjelma kysyy seuraavana salaamiseen käytettävän julkisen avaimen PRIVATE KEY (d,N)

```bash
Pastea kopioimasi yksityinen salausavain PRIVATE KEY (d,N) terminaaliin.
```
Ohjelma kysyy seuraavana purettavan viestin

```bash
Pastea terminaaliin aiemmin salaamasi viesti
```
Ohjelma tulostaa terminaaliin viestin purettuna.

3. Lopetus
```bash
Valitse päävalikosta: q - lopetus
```

### Syötteiden validointi

Syötteille on tehty kevyttä validointia, avainten täytyy olla oikean muotoisia, salattava viesti ei saa olla liian pitkä, purettava viesti ei saa olla tyhjä, etc.

