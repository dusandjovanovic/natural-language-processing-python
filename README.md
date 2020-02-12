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

### Generisanje n-gramova

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

Funkcija se može modifikovati tako da je dužina n-gramova varijabilna po formuli **Broj_indeksa % 7 + 7**.

```python
def generate_ngrams(s, n):
    # konverzija u mala slova
    s = s.lower()
    
    # zamena svih ne-alfanumeričkih znakova razmacima
    # važno je uključiti specifična slova srpskog alfabeta poput ž, š i sličih
    s = re.sub(r'[^a-zA-Z0-9ćčžšđ\s]', ' ', s)
    
    # razbijanje rečenica na tokene, bez praznih tokena
    tokens = [token for token in s.split(" ") if token != ""]
    
    # prolaskom kroz ulazni niz se generišu n-gramovi
    # potrebno je i nadovezati razbijene tokene
    offset = 0
    ngrams = []
    while (offset <= len(tokens)):
        length = offset % n + n
        ngrams.append(tokens[offset:(offset+length)])
        offset = offset + 1
        if (offset + length == len(tokens) + 1):
            break

    return ngrams
```

### Nalaženje verovatnoće svakog n-grama

**Verovatnoća pojavljivanja konkretnog n-grama**, definisanog njegovim indeksom, može se naći kao odnos broja poklapanja uzorka sa ukupnim brojem n-gramova koji su dobijeni od polazng teksta. 

```python
def probability_ngrams(ngrams, index):
    ngram = ngrams[index]
    ngram_found = 0

    for i_ngram in ngrams:
        if (i_ngram == ngram):
            ngram_found = ngram_found + 1

    return ngram_found / len(ngrams)
```

### Ulazni uzorak teksta

Kao primer, izabran je obiman tekst recenzije knjige na srpskom jeziku. Ulazi fajl je prekonfigurisan na putanju `main_file = 'input_text.txt'` i u slučaju pokretanja programa nad drugim uzorkom je potrebno promeniti fajl.

```python
def main():
    contents = read_file(main_file)
    ngrams = generate_ngrams(contents, n=7)

    index = 0
    for ngram in ngrams:
        print(ngram)
        print("Probability of n-gram", probability_ngrams(ngrams, index))
```

Ulazni fajl se učitava, a nakon toga se procesuira pročitani tekst. Neophodno je da fajl bude u `.txt` formatu sa `UTF-8` enkodiranjem. Nakon što se tekst razbije na tokene potrebno je formirati n-gramove prethodno objašnjenom funkcijom `generate_ngrams`. Svaki n-gram se prikazuje na izlazu uz njegovu verovatnoću pojavljivanja u tekstu koja se dobija funkcijom `probability_ngrams`.

### Rezultati

Nakon što se izvrši generisanje svih n-gramova varijabilnih dužina, na ekranu se može videti svaki od njih kao i verovatnoća pojavljivanja istog. U slici ispod se može pogledati deo krajnjeg rezultata. Kako je tekst preobiman, nisu prikazani rezultati kompletne analize.

![alt text][screenshot_end]

[screenshot_end]: meta/screenshot_end.png
