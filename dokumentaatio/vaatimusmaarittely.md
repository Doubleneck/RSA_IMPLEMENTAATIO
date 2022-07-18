# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on RSA avaingeneraattori ja encoder/decoder, jolla voi jolla voi salata ja purkaa viestejä generoitujen suuriin (1024bit) alkulukuihin perustuvien
avainten perusteella.

## Harjoitustyön määrittelyt

-Kuulun TKT:n kandiohjelmaan.
-Dokumentaatio on suomeksi.
-Harjoitustyössä käytetty kieli on Python.
-Vertaisarvioita ajatellen: en osaa juurikaan muita kieliä kuin Pythonia.
-Avainten generoimisessa käytetään:
  -miller-rabin -algoritmia, jolla tuotetaan tarvittavat suuret alkuluvut (algoritmi on propabilistinen, eli takaa että luvut ovat alkulukuja hyvin suurella 
  todennäköisyydellä), joilla tuotetaan avaimissa tarvittava N-komponentti.
  -Laajennettua eukleideen algoritmia tuottamaan salaiseen avaimeen tarvittava d-komponentti.
  -Julkisen avaimen e-komponenttina käytetään yleiseksi standardiksi muodostunutta lukua 65537.
  -"SieveOfEratosthenes" -algoritmi, jota käytetään tuottamaan ensimmäisten alkulukujen sarja varsinaista miller - rabinia optimoimaan.
  
-Algoritmin aika- ja tilavaatimukset:
  (TÄMÄ ON KYLLÄ AIKA HEBREAA MULLE MISTÄ NÄÄ SEURAA...)
  -jos oikein ymmärsin niin tässä on kyseessä "repeated squaring" algoritmi, jonka aikavaatimus on O(k log3 n), missä n on alkulukukandidaatti?
  -tilavaatimus?? 

-Lähteitä:
    -https://fi.wikipedia.org/wiki/RSA
    -https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    -https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm

## Käyttäjät

Sovellukselle ei määritellä erikseen käyttäjiä. 

## Käyttöliittymäluonnos

Sovelluksella on tekstikäyttöliittymä. Jatkokehitysideana graafinen käyttöliittymä. 


## Perusversion tarjoama toiminnallisuus

### Ei kirjautumista


- [ ] käyttäjä voi luoda yksityisen ja julkisen avaimen avainparin
- [ ] käyttäjä voi salata viestin generoidulla julkisella avaimella
- [ ] käyttäjä voi purkaa viestin generoidulla yksityisellä avaimella
