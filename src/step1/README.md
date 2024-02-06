# Steg 1

I steg 1 skal dere finne ut når låtene begynner og slutter, samt plukke opp hint som kommer i praten mellom låtene.
For å gjøre dette må dere interagere med dataen fra radioen.

All kode til oppgave 1 skrives i funksjonen `handle()`, i filen [radio.py](src/step1/radio.py). Denne funksjonen tar inn tre argumenter:
- `store` er en enkel keyValue-store dere kan benytte for å lagre verdier mellom kjøringer.
- `publisher` er publisheren dere skal benytte for å signalisere hendelser til systemet.
- `events` er dataen fra radiokanalen.

Undersøk funksjonaliteten og metodene som nnn eksponerer, og løs oppgaven!

For å bli ferdig med oppgaven skal dere altså:

1. Finne alle hint, og publisere de til tjenesten.
2. Publisere låtnavnet til tjenesten når en låt begynner.
3. Publisere låtnavnet til tjenesten når en låt er ferdigspilt.

For å se om dere har gjort oppgaven riktig pusher dere koden til main-branchen og sjekker om testene passer i CI/CD-pipelinen [OBS: TSJ - WIP].

[Til TSJ: hadde vært veldig nice om vi kunne hatt disse tipsene i en collapsible eller om vi putter de i en egen readme]

Tips:

- For å finne ut om en melding fra radioen inneholder sang eller tale kan dere sjekke typen på dataen
