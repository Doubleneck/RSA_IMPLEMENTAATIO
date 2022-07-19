- Ennakkotutkimukset (kesäkuussa):
    - Tein tätä muutaman päivän etukenoon, kun tuli tuntuma, että aloittelijana tää on vähän kuitenkin osaamisen rajoilla.
    - Etsin tarvittavat algoritmit: Olennaisimmat ovat miller-rabin ja extended eucleidian.
    - Vaikkei varsinaisesti liitykään RSA:han, niin käytin jonkun verran aikaa siihen, miten stringit muutetaan binääreiksi, itselleni pääosin uusi asia. 
      Nopeuden kannalta kuitenkin selvästi oleellinen. Olihan noista bittimaskeista jotain tietekoneen toiminnan kurssilla.
    - alkuluento, ohjelman kasausta, testejä rsa-funktioille ja string/bin muunnoksien funktioille.

- Miten ohjelma on edistynyt
    - ainakin sain yleisen ohjelmarakenteen läjään OHTE-matskuilla. Coverage mm. puuttuu, samoin dokumentaatiota.
    - Olen kokeillut jonkun verran ja tässä vaiheessa miller-rabinin läpäisevät alkuluvut näyttäis menevän oikein.
    
- Mitä opin tällä viikolla / tänään?
    - Että tauon jälkeen pythonin self-määreen käyttö olikin vähän unohtunut- 
    - Testaaminen meneekin mielenkiintoiseksi:
      Kun miller-rabin testaa "todennäköisesti", että joku voisi olla alkuluku, niin miten testata sitä toimiiko tuo testi oikein?
      Tässä syntyy helposti kehämäistä päättelyä, jos yrittää jotain simppeliä unit-testiä, poislukien tietenkin triviaalit ei-alkuluvut,
      joita on helpohko varmaankin testata.
    
- Mikä jäi epäselväksi tai tuottanut vaikeuksia? 
    - Miller-rabinissa "ensimmäinen kierros" on aika selvä, jos kongruenssi on 1 tai -1, niin puolletaan alkuluvun todennäköisyyttä.
      Mut sitten tuo seuraava pätkä, minkä verran iteraatioita tehdään ettei jää esim. looppaamaan. En ihan täysin hahmota vieläkään tuota kohtaa.
      Se näyttäis toimivan, olen kasannut sitä osaa parin videon perusteella, sehän on kriittinen lähinnä nopeuden kannalta jos tekee turhia kierroksia.
      Ilmeisesti noin 20 kerran iteraatio erilaisilla 1 < a < k-1 (random)arvoilla tuottaa jo melko hyvän osumatodennäköisyyden.
      Sen perustelu oli mulle selvästi liian hankala.
    - Testasin tota suoraan netistä pöllityllä GCD extended euclidian algoritmin pätkällä ja sain isoilla avaimilla menemään kumpaankin suuntaan.
    - pienten alkulukujen generaattorin "sieve_of_eratosthenes" (tässä käytän 200 ensimmäisen alkuluvun listaamiseen) otin valmiina, se on kuitenkin tässä       vaan optimoimassa sitä, ettei ihan jokaista tarvitse käydä läpi raskaammalla Miller-Rabinilla.

- Mitä teen seuraavaksi?
    - Pseudokoodin avulla extended eucleidianin, sen jälkeen tän pitäisi olla jo avainten generointi ja salaus/purku -kunnossa.
    - Löysin nopeuttavan pow:n joka tekee optimoimmin laskemalla ilmeisesti jotenkin jakojäännösten avulla huomattavasti nopeammin, mutta en ainakaan vielä
      käsitä miten se toimii. 
