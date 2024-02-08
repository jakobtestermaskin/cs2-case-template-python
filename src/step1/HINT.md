# Hint
- For å finne ut om en melding fra radioen inneholder sang eller tale kan dere sjekke typen på dataen.
- `json.dumps(arg, indent=4)` gjør ting mer lettleselig under printing av radioen.
- Bruk `datetime`-biblioteket, og `datetime.datetime.utcNow().isoFormat()` om du vil tracke tidspunkter(systemet gir 1 minutt slingringsmonn).

Argumentene inn i `handle()`:
- `store` er en enkel keyValue-store dere kan benytte for å lagre verdier mellom kjøringer.
- `publisher` er publisheren dere skal benytte for å signalisere hendelser til systemet.
- `events` er dataen fra radiokanalen.
