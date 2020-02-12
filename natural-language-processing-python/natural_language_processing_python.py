import re
from nltk.util import ngrams

main_file = 'input_text.txt'

def read_file(file_path):
    file = open(main_file, "r", encoding = "utf8")
    contents = file.read()
    file.close()
    return contents

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

def probability_ngrams(ngrams, index):
    ngram = ngrams[index]
    ngram_found = 0

    for i_ngram in ngrams:
        if (i_ngram == ngram):
            ngram_found = ngram_found + 1

    return ngram_found / len(ngrams)

def main():
    contents = read_file(main_file)
    ngrams = generate_ngrams(contents, n=7)

    index = 0
    for ngram in ngrams:
        print(ngram)
        print("Probability of n-gram", probability_ngrams(ngrams, index))
        print("\n")
        index = index + 1

  
if __name__== "__main__":
    main()