# Steg 2

Steg 2 blir kjørt hver gang steg to rapporterer at en sang er ferdig. I denne skal du bruke informasjonen fra hintene i steg 1 for å gjennomføre betalinger til artistene. Finn ut hvor mye en artist skal betales, og gjennomfør denne betalingen.
Her trenger du å jobbe med filen [payment_service.py](src/step2/payment_service.py).

I tillegg kand et være lurt å kode inn informasjonen du lærer fra å ha fullført steg 1. Det er ikke nødvendig med noen databaseintegrasjoner i denne oppgaven.

Ettersom flyttal kan by på problemer, nettopp fordi de i natur er flyttal, benytter man ofte en [valuttas laveste enhet](https://stripe.com/docs/currencies#zero-decimal). Derfor benytter vi kroner når vi gjennomfører en betaling!
