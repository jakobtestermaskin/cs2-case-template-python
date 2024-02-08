# Steg 1

I steg 1 skal dere finne ut når låtene begynner og slutter, samt plukke opp hint som kommer i praten mellom låtene.
For å gjøre dette må dere interagere med dataen fra radioen.

All kode til oppgave 1 skrives i funksjonen `handle()`, i filen [radio.py](src/step1/radio.py). 
Denne funksjonen tar inn tre argumenter: `store`, `publisher` og `events`. 
Sjekk ut andre filer, print og undersøk for å finne ut hvordan disse kan hjelpe dere med å løse oppgaven.

For å bli ferdig med oppgaven skal dere altså:

1. Finne alle hint, og publisere de til tjenesten.
2. Publisere låtnavnet til tjenesten når en låt begynner.
3. Publisere låtnavnet til tjenesten når en låt er ferdigspilt.

For å se om dere har gjort oppgaven riktig pusher dere koden til main-branchen og sjekker om testene passer i CI/CD-pipelinen.

Til slutt, to bemerkninger for å løse oppgaven:
- Radioen går 24/7, så dere behøver ikke håndtere tilfeller hvor det ikke kommer mer data.
- Når en sang avsluttes, kan det gå flere minutter med prat før neste sang begynner.

Det ligger også noen hint [her](HINT.md) som dere kan sjekke ut etter hvert. Lykke til! :star2:
