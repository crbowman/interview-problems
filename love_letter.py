from collections import Counter

LETTER_STRINGS = ["This is my love letter.",
                  "Jived fox nymph grabs quick waltz.",
                  "brown fox"]
NEWS_STRINGS = ["The quick brown fox jumps over the lazy dog.",
                "The \t quick \n brown fox jumps over the lazy dog."]


def love_letter(letter, newspaper):
    l_set = set(letter)
    n_set = set(newspaper)
    if not l_set.issubset(n_set):
        return False
    l_freqs = dict(Counter(list(letter)))
    n_freqs = dict(Counter(list(newspaper)))
    for f in l_freqs:
        if l_freqs[f] > n_freqs[f]:
            return False
        else:
            continue
    return True
