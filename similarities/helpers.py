from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    ls1 = set(a.splitlines())
    ls2 = set(b.splitlines())

    similar = ls1.intersection(ls2)

    return similar


def sentences(a, b):
    """Return sentences in both a and b"""

    #  set_tokenize recognizes english sentences.
    #  split('.') does not work for this, because sentences can end in !, ?, etc.

    ls1 = set(sent_tokenize(a))
    ls2 = set(sent_tokenize(b))

    similar = ls1.intersection(ls2)

    return similar


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    ls1 = []
    ls2 = []

    for i in range(0, len(a), 1):
        if len(a[i:i+n]) == n:
            ls1.append(a[i:i+n])

    for i in range(0, len(b), 1):
        if len(b[i:i+n]) == n:
            ls2.append(b[i:i+n])

    ls1 = set(ls1)
    ls2 = set(ls2)
    similar = ls1.intersection(ls2)

    return similar

