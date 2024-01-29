# CS2 Caseoppgave

Velkommen til CS2 caseoppgave! :rocket:

Casen består av 4 steg, der de tre første omhandler CS Radio og det siste spillet Battleship.

CS Radio er vår helt egne radiokanal for å dispatche meldinger.
Foreløpig må vi betale en flat sum til hver artist vi featurer på radiokanalen vår, ettersom vi mangler funksjonalitet for å betale artistene for hver gang en låt spilles. Vi ønsker oss en løsning som kan registrere når låter starter og slutter, så vi kan spare penger. Det er her dere kommer inn, for å hjelpe oss med dette :partying_face:

[TODO TSJ: litt info om tjenesten, hvilke filer de trenger å se på osv - typ litt av det Jakob kommer til å si før de begynner]

## Oppgaver

### Steg 1 [WIP]

I steg 1 skal dere få innsikt i dataen fra radioen.
Som i en vanlig radiosending spilles det sanger og prates mellom disse.
For å se hvordan dataen fra radioen ser ut kan dere kjøre [simulate.py](src/step1/simulate.py) i terminalen, som simulerer en del av en radiosending.

```bash
python3 simulate.py
```

Dere kan da se at dataen kommer i python dictionaries.
Vi vil at dere skal persistere denne dataen fra dictionaries til objekter.
For å se om dere har gjort oppgaven riktig pusher dere koden til main-branchen og sjekker om testene passer i CI/CD-pipelinen [OBS: TSJ - WIP].

- [WIP]: Vi må ha tester som sjekker at dette gjøres riktig. Kanskje en CI/CD-pipeline som sjekker om objektene er på riktig format?
- [TODO]: link til filen de skal jobbe i når oppgaven er laget

---

### Steg 2

I steg 2 skal dere finne ut når låtene begynner og slutter, samt plukke opp hint som kommer i praten mellom låtene.
For å gjøre dette må dere interagere med dataen fra radioen.

[Til TSJ: flytte noe av dette til tips-seksjon og heller skrive at de burde se på argumentene som passes til funksjonen?]

All kode til oppgave 1 skrives i funksjonen handle(), i filen src/step1/radio.py

`store` er en enkel keyValue-store dere kan benytte for å lagre verdier mellom kjøringer.

`publisher` er publisheren dere skal benytte for å signalisere hendelser til systemet.

`events` er dataen fra radiokanalen.

Undersøk funksjonaliteten og metodene som nnn eksponerer, og løs oppgaven!

For å bli ferdig med oppgaven skal dere altså:

1. Finne alle hint, og publisere de til tjenesten.
2. Publisere låtnavnet til tjenesten når en låt begynner.
3. Publisere låtnavnet til tjenesten når en låt er ferdigspilt.

[Til TSJ: hadde vært veldig nice om vi kunne hatt disse tipsene i en collapsible eller om vi putter de i en egen readme]

Tips:

- For å finne ut om en melding fra radioen inneholder sang eller tale kan dere sjekke typen på dataen

---

### Steg 3 [WIP]

Steg tre blir kjørt hver gang steg to rapporterer at en sang er ferdig. I denne skal du bruke api-ene for å finne ut hvor mye en artist skal betales, og så gjennomføre denne betalingen.
Her trenger du å jobbe med filen [payment_service.py](src/step2/payment_service.py).

---

### Steg 4 - Battleship [WIP]

[TODO]

## Generelle tips

- For å simulere systemet, kan du kjøre følgende kommando fra `src`: `python3 simulate.py`. Alt som printes i `handle()` vil da printes i konsollen.
- [TODO: fjern om steg 1 om objekter blir implementert?] Sliter du med å få oversikt? Prøv å strukturere dataen, enten ved hjelp av klasser eller andre datastrukturer
- Lag hjelpefunksjoner for å bryte opp koden
- Når en sang avslutter, kan det gå flere minutter med prat før neste sang begynner.
- Radioen går 24/7, så dere behøver ikke håndtere tilfeller hvor det ikke kommer mer data.

### Utvikling

- Ikke installer pakker, da kræsjer systemet :^)
- `json.dumps(arg, indent=4)` gjør ting mer lettleselig under printing av radioen
- Bruk `datetime`-biblioteket, og `datetime.datetime.utcNow().isoFormat()` om du vil tracke tidspunkter(systemet gir 1 minutt slingringsmonn).

# Debugging

Å kunne lese loggene til distribuerte systemer er helt avgjørende for å kunne klare å jobbe med dem.
Derfor har vi laget brukere som dere enkelt kan logge inn i AWS med.

For å hente ressursene du trenger for å gjøre debugging må du bruke linkene som er oppgitt under for å komme til riktig steg. Aller først må du logge inn i AWS.
Benytt følgende lenke for å logge inn:
https://cs2case.signin.aws.amazon.com/console

IAM User name: `<group-number>-console-access`
Password: Dette får du i DM fra Jakob

## Ressurser

Det er forskjellige ressurser du kan hente ned. Enten kan du logge inn i AWS og lese loggene til funksjonene, eller så kan du hente ned events som er blitt publisert.

### Cloudwatch (Logger)

Vi benytter CloudWatch for å lese loggene til lambda-filene.
Her finner du log-gruppen for lambdaen din:

| Step   | Link                                                                                                                                                                     |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Step 1 | https://eu-west-1.console.aws.amazon.com/cloudwatch/home?region=eu-west-1#logsV2:log-groups/log-group/$252Faws$252Flambda$252Fcs2-case-st24-<group-number>-step1-default |
| Step 2 | https://eu-west-1.console.aws.amazon.com/cloudwatch/home?region=eu-west-1#logsV2:log-groups/log-group/$252Faws$252Flambda$252Fcs2-case-st24-<group-number>-step2-default |

### Events

Benytt scriptet [get_events.py](src/get_events.py).

Hvis du er stasjonert i src-mappen, kan du gjøre følgende:

```bash
python3 get_events.py
```

Du kan også velge om du ønsker song_ended events (song_ended), hint_evnets (hint), eller payment_events (payment) ved å benytte ordene i parentes som param til programmet. For eksempel:

```bash
python3 get_events.py song_ended
```

# Virituelt miljø med Python

Dersom du ønsker et virituelt miljø med python, kan du enkelt opprette et med `bash python3 -m venv venv`. Nødvendige pakker finner du local_development_requirements.txt.

Aktiver miljøet med `bash source venv/bin/activate`, deretter installerer du pakker med `bash pip install -r local_development_requirements.txt`

Evt: `bash python3 -m pip install -r local_development_requirements.py`, dersom du ikke har pip i path-en.
