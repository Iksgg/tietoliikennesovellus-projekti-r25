# Tietoliikenteen sovellus Projekti Syksy 2025 R25
Tietoliikenteen sovellus projekti joka suoritetaan osana Tieto- ja viestintätekniikan opintoja. Projektissa Mitataan kiihtyvyysanturi dataa, välitetään data Rasperry pi:n avulla Linux palvelimella olevaan tietokantaan ja mittaus dataa käytetään koneoppimisessa.

## Arkkitehtuuri
![Arkkitehtuuri kuva](documents/arkkitehtuuri_kuva.png)

## Tavoitteet
### Mittaus
Mittaukseen käytetään GY-61 3-akselinen kiihtyvyysanturia ja Nordik nRF5340 devKit alustaa. Mittaus edellyttää ohjelman luontia joka kykeneen ottamaan vastaan anturin mittaamat arvot ja lähettää ne BLE yhteyden yli.

Mittaus tapahtuu 100 hertsin näyteistys taajuudella ja suoritetaan kuudessa eri asennossa noin 10 sekunnin ajan. Tämä taekoittaa että kokonaisuutena mittauksesta saadaan 6000 näytettä, eli 1000 näytettä per asento. mittaus ja lähetys tapahtuu yhden aikaisesti. Mittaus tiedot lähetetään BLE Notifikaationa jotka vastaan ottaja tilaa.

### Tiedonsiirto
Tiedon siirtoon käytetään BLE ja TCP yhteyksiä Mitta laitteisto välittää mittaus tiedon BLE yli rasperry pi:lle joka toimii IOT Gatewaynä ja siirtää vastaan otetun datan Linux palvelimella olevaan tietokantaan. Tietokannasta dataa haetaan TCP Clientin avulla csv tiedostoon.

### Hyödyntäminen
Kerättyä ja säilöttyä dataa hyödynnetään koneoppimismallin kouluttamisessa. Käytettävä malli on K-means algoritmi joka ottaa data setin x,y ja z pisteet ja kuusi eri keskipistettä jotka vastaavat jokaista asentoa. Nämä keskipisteet palautetaan keskipisteet.h tiedostona.

## Confucion Matrix
![Confucion matrix tähän jahka sen on saatu tehtyä](documents/)


## Tekijät
- Hietamäki Valtteri
- Ikäläinen Sami
