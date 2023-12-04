from collections import Counter


def valid_anagram(s, t):
    return Counter(s) == Counter(t)
