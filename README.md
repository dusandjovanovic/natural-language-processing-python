# Procesiranje prirodnih jezika

**Zadatak:**
Pronaći tekst na srpskom jeziku ne kraći od 6000 karaktera, a zatim ga prevesti u n-gram model nad rečima, dužine Broj_indeksa % 7 + 7. Zatim odrediti verovatnoće pojavljivanja svakog elementa.

- Koji je model i koje dužine najbolje primeniti za konkretan problem?
- Zašto?

**N-gram** je kontinualni niz n elemenata u rečenici. N može biti 1, 2 ili bilo koji drugi pozitivan prirodan broj ali se obično ne uzimaju velike vrednosti jer se retko pojavljuju u tekstovima. Kada se primenjuju tehnike NLP-a potrebno je generisati n-gramove na osnovu ulaznog teksta.

U opštem slučaju, ulazni tekst je skup karaktera.

```python
s = "Natural-language processing (NLP) is an area of computer science " \
    "and artificial intelligence concerned with the interactions " \
    "between computers and human (natural) languages."
```

Ako bi se generisala lista bi-gramova iz prethodne rečenice, očekivani izlaz bio bi:

```python
[
    "natural language",
    "language processing",
    "processing nlp",
    "nlp is",
    "is an",
    "an area",
    ...
]
```

Najprostija varijanta funkcije koja obavlja generisanje n-gramova na osnovu ulaznog teksta:

```python
import re

def generate_ngrams(s, n):
    # konverzija u mala slova
    s = s.lower()
    
    # zamena svih ne-alfanumeričkih znakova razmacima
    # važno je uključiti specifična slova srpskog alfabeta poput ž, š i sličih
    s = re.sub(r'[^a-zA-Z0-9ćčžšđ\s]', ' ', s)
    
    # razbijanje rečenica na tokene, bez praznih tokena
    tokens = [token for token in s.split(" ") if token != ""]
    
    # zip funkcijom se generišu n-gramovi
    # potrebno je i nadovezati razbijene tokene
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]
```

Ova funkcija se bazira na nepromenljivom **ulaznom argumentu n** kako bi generisala n-gramove. Koristi `zip` funkciju koja formira generator čiji je zadatak da agregira elemente različitih listi. Važno je prilikom korišćenja regularnog izraza za filtriranje uključiti i **specifična slova srpskog alfabeta**.
