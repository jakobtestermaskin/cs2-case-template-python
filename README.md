# TODO: Rewrite README

## Hvordan jobbe med stepsene?

Se (TJS: fikser dere link?) debugging for informasjon om hvordan jobbe med prosjektet.

Velkommen til CS 2 caseoppgaven!!

Dette blir dritkul!

I steg 1 og 2 skal dere jobbe med CS RADIO!

Vår helt egne radiokanal for å dispatche meldinger.
Dessverre har vi ikke implementert en funksjon for å betale artistene for hver gang de spilles. Dette betyr at vi må betale mye høyere satser for å spille hver artist.

Derfor ønsker vi at dere lager funksjoner for å finne ut når sanger starter, når de slutter og deretter sende dette videre i steg 1. Bruk filen "radio.py" og ikke rør noe annet.

Steg to blir kjørt hver gang steg 1 rapporterer at en sang er ferdig. I denne skal du bruke api-ene for å finne ut hvor mye en artist skal betales, og så gjennomføre denne betalingen.
Her trenger du å jobbe med filen "step2_handler.py"

OG TIL TSJ:
Please! Gjør endringer i dette repoet!!

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

Benytt scriptet (TJS: Link plz) get_events.py

Hvis du er stasjonert i src-mappen, kan du gjøre følgende:

```bash
python3 get_events.py
```

Du kan også velge om du ønsker song_ended events (song_ended), hint_evnets (hint), eller payment_events (payment) ved å benytte ordene i parentes som param til programmet. For eksempel:

```bash
python3 get_events.py song_ended
```
