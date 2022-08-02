
# Toteutusdokumentti

Sovellus on 1024bit RSA-avaingeneraattori ja encoder/decoder tekstikäyttöliittymällä.

## Algoritmit

Pääasiallisesti toteutus perustuu tähän artikkeliin, mistä löytyy salauksen toimintaperiaate ja rakenne [wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem)), sekä mm. Fermat´n pieneen lauseeseen perustuva matemaattinen todistus.

Miller-Rabin algoritmi [wikipedia](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test))
Laajennettu Eukleideen algoritmi [wikipedia](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)


## Tila- ja aika-vaatimukset

Avaimet:

Ensin suoritettava random-alkuluvun luominen ja matalan kynnyksen alkulukutestaus tapahtuu vakioajassa O(1).
(Alkulukuja esiintyy tässä kokoluokassa noin parinsadan kokonaisluvun välein, ja etsintä tehdään korkeintaan muutaman kerran noin 200 sarjalla)

Miller-rabinin aikavaatimus on O(k log3 n), missä n on testattava luku (2^511-2^512) ja k iteraatioiden määrä (40)
Laajennetun Eukleideen algoritmin aikavaatimus on O(log(min(a, b))).[aikavaatimus](https://www.scaler.com/topics/data-structures/extended-euclidean-algorithm)

Avainten tuottamisen aikavaatimus on siis O(k log3 n) + O(log(min(a, b))). 

Salaaminen ja purku:

Jos oletetaan, että modulaarilaskenta toimii aikavaatimuksella  O(log(n)), missä n on mikä tahansa kokonaisluku, niin eksponenttifunktioiden laskennan aikavaatimus on salauksen ja purun yhteydessä O((log n)^3))[aikavaatimus](https://www.quora.com/What-is-the-complexity-of-RSA-cryptographic-algorithm)

Tilavaatimus:

Algoritmin tilavaatimus on vakio O(1) suhteessa viestin kokoon, eli salauksen kokoluokka N (tässä 1024)



## Ohjelman rakenne

[luokkakaavio]() PUUTTUU

