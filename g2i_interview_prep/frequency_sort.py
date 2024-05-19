from collections import Counter


def frequency_sort_with_libraries(s: str) -> str:
    freq = Counter(s)

    sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    return ''.join([char * count for char, count in sorted_chars])


def frequency_sort_without_libraries(s: str) -> str:
    freq = {}
    for char in s:
        freq[char] = 1 + freq.get(char, 0)

    freq_list = [(char, count) for char, count in freq.items()]

    freq_list_sorted = sorted(freq_list, key=lambda x: (-x[1], x[0]))

    return ''.join([char * count for char, count in freq_list_sorted])
