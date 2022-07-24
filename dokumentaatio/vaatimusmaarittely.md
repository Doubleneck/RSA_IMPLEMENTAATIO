# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on RSA avaingeneraattori ja encoder/decoder, jolla voi jolla voi salata ja purkaa viestejä generoitujen suuriin (1024bit) alkulukuihin perustuvien avainten perusteella.

## Harjoitustyön määrittelyt

- Kuulun TKT:n kandiohjelmaan.
- Dokumentaatio on suomeksi.
- Harjoitustyössä käytetty kieli on Python.
- Vertaisarvioita ajatellen: en osaa juurikaan muita kieliä kuin Pythonia.

- RSA-avainten generointi tuottaa avainparin: julkisen avaimen, joka on lukupari (N,e) ja yksityisen avaimen, joka on lukupari (N,d).
- RSA-avainten suuruusluokka on 1024bit.
- toteutan havainnollistamisen niin, että salattava data annetaan tekstimuodossa, ja se muutetaan binääreiksi ja suureksi luvuksi, ja sama vastaavasti purkaessa toisin päin. Näin toteutettuna viestin pituus rajoittuu avaimen kokoon.

- Avainten generoimisessa käytetään:
  - miller-rabin -algoritmia, jolla tuotetaan tarvittavat suuret alkuluvut (algoritmi on propabilistinen, eli takaa että luvut ovat alkulukuja hyvin    suurella todennäköisyydellä), joilla tuotetaan avaimissa tarvittava N-komponentti.
  - Laajennettua eukleideen algoritmia tuottamaan salaiseen avaimeen tarvittava d-komponentti.
  - Julkisen avaimen e-komponenttina käytetään yleiseksi standardiksi muodostunutta lukua 65537.
  - "SieveOfEratosthenes" -algoritmi, jota käytetään tuottamaan ensimmäisten alkulukujen sarja varsinaista miller - rabinia optimoimaan.
  
- Salauksessa annetaan syötteeksi generoitu julkinen avain ja salattava viesti, ja vastaavasti purkaessa syötteeksi annetaan yksityinen avain ja kryptattu viesti.


- Algoritmin aika- ja tilavaatimukset:
  (TÄMÄ ON KYLLÄ AIKA HEBREAA MULLE MISTÄ NÄÄ SEURAA...)
  - jos oikein ymmärsin niin tässä on kyseessä "repeated squaring" algoritmi, jonka aikavaatimus on O(k log3 n), missä n on alkulukukandidaatti ja k testausiteraatioiden määrä?
  - tilavaatimus?? 

- Lähteitä:
    - https://fi.wikipedia.org/wiki/RSA
    - https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    - https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb
    - https://www.youtube.com/watch?v=qdylJqXCDGs (Miller Rabin yksinkertaistettuna, puuttuu tapaus jossa jää loputtomiin looppaamaan?)
    - https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm (tässä implementaatiossa käytetty algoritmi löytyy täältä pseudokoodina)
    - http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html (Laajennettu Euklideen algoritmi ja inverse kompaktisti selitettynä)

## Käyttäjät

Sovellukselle ei määritellä erikseen käyttäjiä. 

## Käyttöliittymäluonnos

Sovelluksella on tekstikäyttöliittymä. Jatkokehitysideana graafinen käyttöliittymä. 

## Perusversion tarjoama toiminnallisuus

### Ei kirjautumista

- [x] käyttäjä voi luoda yksityisen ja julkisen avaimen avainparin
- [x] käyttäjä voi salata viestin generoidulla julkisella avaimella
- [x] käyttäjä voi purkaa viestin generoidulla yksityisellä avaimella
