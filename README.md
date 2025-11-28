# Tietoliikenteen sovellus Projekti Syksy 2025 R25
Tietoliikenteen sovellus projekti joka suoritetaan osana Tieto- ja viestintätekniikan opintoja. Projektissa Mitataan kiihtyvyysanturi dataa, välitetään data Rasperry pi:n avulla Linux palvelimella olevaan tietokantaan ja mittaus dataa käytetään koneoppimisessa.


## Arkkitehtuuri
![Arkkitehtuuri kuva](documents/arkkitehtuuri_kuva.png)

## Tavoitteet
### Mittaus
Mittaukseen käytetään kiihtyvyys anturia ja Nordik nRF5340 devKit alustaa. Mittaus edellyttää ohjelman luontia joka kykeneen ottamaan vastaan anturin mittaamat arvot ja lähettää ne BLE yhteyden yli.

### Tiedonsiirto
Tiedon siirtoon käytetään BLE ja TCP yhteyksiä Mitta laitteisto välittää mittaus tiedon BLE yli rasperru pi:lle joka toimii IOT Gatewaynä ja siirtää vastaan otetun datan Linux palvelimella olevaan tietokantaan. Tietokannasta dataa haetaan TCP Clientin avulla csv tiedostoon.

### Hyödyntäminen
Kerättyä ja säilöttyä dataa hyödynnetään koneoppimismallin kouluttamisessa.


## Tekijät
- Hietamäki Valtteri
- Ikäläinen Sami
