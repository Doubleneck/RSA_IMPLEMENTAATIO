
# Toteutusdokumentti

Sovellus on 1024bit RSA-avaingeneraattori ja encoder/decoder tekstikäyttöliittymällä.

## Algoritmit

Pääasiallisesti toteutus perustuu tähän artikkeliin, mistä löytyy salauksen toimintaperiaate ja rakenne [wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem)), sekä mm. Fermat´n pieneen lauseeseen perustuva matemaattinen todistus.

Miller-Rabin algoritmi [wikipedia](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test))
Laajennettu Eukleideen algoritmi [wikipedia](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)


## Tila- ja aika-analyysi

Purkamisen ja salaamisen aika-analyysi on triviaali, kyseessä on yksinkertainen suurten lukujen 

Ensin suoritettava random-alkuluvun luominen ja matalan kynnyksen alkulukutestaus tapahtuu vakioajassa O(1).
(Alkulukuja esiintyy tässä kokoluokassa noin parinsadan kokonaisluvun välein)

Miller-rabinin aikavaatimus on O(k log3 n), missä n on testattava luku (2^511-2"512) ja k iteraatioiden määrä (40)
Laajennetun Eukleideen algoritmin aikavaatimus on O(log(min(a, b))).[aikavaatimus](https://www.scaler.com/topics/data-structures/extended-euclidean-algorithm)

## Ohjelman rakenne

[luokkakaavio]()

