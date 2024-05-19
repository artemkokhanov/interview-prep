def most_frequent_char(s: str) -> str:
    freq = {}

    for char in s:
        freq[char] = 1 + freq.get(char, 0)

    max_char = max(freq, key=freq.get)

    return max_char


def most_frequent_char_without_predefined_functions(s: str) -> str:
    freq = {}

    for char in s:
        freq[char] = 1 + freq.get(char, 0)

    max_char = ''
    max_count = 0

    for char in freq:
        if freq[char] > max_count:
            max_char = char
            max_count = freq[char]

    return max_char


s1 = "tree"
s2 = "cccaaa"
s3 = "Aabb"

print(most_frequent_char(s1))
print(most_frequent_char(s2))
print(most_frequent_char(s3))
