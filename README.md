# TODO: Rewrite README

## Hvordan jobbe med stepsene?

Se (TJS: fikser dere link?) debugging for informasjon om hvordan jobbe med prosjektet.

Velkommen til CS 2 caseoppgave!

I steg 1, 2 og 3 skal dere jobbe med CS Radio!

CS radio er vår helt egne radiokanal for å dispatche meldinger.
Foreløbig må vi betale en flat sum til hver artist vi featurer på radiokanalen vår, ettersom vi mangler funksjonalitet for å betale artistene for hver gang en låt spilles. Vi ønsker oss en løsning som kan registrere når låter starter og slutter, så vi kan spare penger

🥳Her kommer dere inn!🥳

## Oppgave 1

1. Finn alle hint, og publiser de til tjenesten.
2. Finn ut når låtene begynner, og publiser informasjonen til tjenesten.
3. Finn ut når låtene slutter, og publiser informasjonen til tjenesten.

### Utvikling
All kode til oppgave 1 skrives i funksjonen handle(), i filen src/step1/radio.py

`store` er en enkel keyValue-store dere kan benytte for å lagre verdier mellom kjøringer.

`publisher` er publisheren dere skal benytte for å signalisere hendelser til systemet.

`events` er dataen fra radiokanalen.

Undersøk funksjonaliteten og metodene som nnn eksponerer, og løs oppgaven!

### Ting å tenke på
- Ikke installer pakker, da kræsjer systemet :^)
- Bruk `datetime`-biblioteket, og `datetime.datetime.utcNow().isoFormat()` om du vil tracke tidspunkter(systemet gir 1 minutt slingringsmonn).
- For å simulere systemet, kan du kjøre følgende kommando fra `src`: `python3 simulate.py`. Alt som printes i `handle()` vil da printes i konsollen.
- Radioen går 24/7, så dere behøver ikke håndtere tilfeller hvor det ikke kommer mer data.


### Tips
- json.dumps(arg, indent=4) gjør ting mer lettleselig
- Lag hjelpefunksjoner for å bryte opp koden
- Sliter du med å få oversikt? Prøv å strukturere dataen, enten ved hjelp av klasser eller andre datastrukturer
- Når en sang avslutter, kan det gå flere minutter med prat før neste sang begynner.


## Oppgave 2

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
