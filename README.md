# CS2 Caseoppgave

Velkommen til CS2 caseoppgave! :rocket:

Casen består av to hoveddeler: CS Radio og spillet Battleship.

## CS Radio

CS Radio er vår helt egne radiokanal for å dispatche meldinger.
Foreløpig må vi betale en flat sum til hver artist vi featurer på radiokanalen vår, ettersom vi mangler funksjonalitet for å betale artistene for hver gang en låt spilles. 
Vi ønsker oss en løsning som kan registrere når låter starter og slutter, så vi kan spare penger. 
Det er her dere kommer inn, for å hjelpe oss med dette :partying_face:

Koden dere skal jobbe med ligger i mappene `step1` og `step2`. 
Det er bare å kikke rundt i mappene for å forstå hvilke funksjoner som finnes og som kan være til hjelp under løsingen av oppgavene.
I tillegg ligger det noen generelle tips lengre ned i denne README-en, samt noen hint i egne README-er i hver av mappene.

### Steg 0 

Til å begynne med anbefaler vi dere å få litt innsikt i dataen fra radioen.
Som i en vanlig radiosending spilles det sanger og prates mellom disse.
For å se hvordan dataen fra radioen ser ut kan dere kjøre [simulate.py](src/step1/simulate.py) i terminalen, som simulerer en del av en radiosending.

```bash
python3 simulate.py
```

Dere kan da se at dataen kommer i python dictionaries.
For å få en bedre innsikt i dataen kan dere for eksempel persistere dataen fra dictionaries til objekter. 
Dette er ikke noe dere er nødt til å gjøre, men kan være en fin intro til oppgavene.

For å løse de neste delene av CS Radio-oppgaven kan dere gå inn i README-ene til [step1](src/step1/README.md) og [step2](src/step2/README.md) for å lese oppgavebeskrivelsene. 


## Battleship

Når dere er ferdig med CS Radio-oppgaven kan dere lese oppgavebeskrivelsen for Battleship [her](src/battleship/README.md).


# Generelle tips

- Ikke installer pakker, da kræsjer systemet :^)
- Lag hjelpefunksjoner for å bryte opp koden.
- Det ligger en del funksjoner som kan være til hjelp i ulike filer. Bare å trykke seg rundt for å finne hjelpemidler!


## Debugging

Å kunne lese loggene til distribuerte systemer er helt avgjørende for å kunne klare å jobbe med dem.
Derfor har vi laget brukere som dere enkelt kan logge inn i AWS med.

For å hente ressursene du trenger for å gjøre debugging må du bruke linkene som er oppgitt under for å komme til riktig steg. Aller først må du logge inn i AWS.
Benytt følgende lenke for å logge inn:
https://cs2case.signin.aws.amazon.com/console

IAM User name: `<group-number>-console-access`
Password: Dette får du i DM fra Jakob

### Ressurser

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
