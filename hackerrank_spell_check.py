import re
from collections import Counter

def words(text): return re.findall(r'\w+', text.lower())

# A very basic vocabulary for demonstration
WORDS = Counter(words("a an the is are was were hello world apple banana orange computer science spelling"))

def P(word, N=sum(WORDS.values())): 
    return WORDS[word] / N if N > 0 else 0

def correction(word): 
    return max(candidates(word), key=P)

def candidates(word): 
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words_list): 
    return set(w for w in words_list if w in WORDS)

def edits1(word):
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

if __name__ == "__main__":
    print(correction("speling"))
