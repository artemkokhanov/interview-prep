from collections import defaultdict


def group_anagrams(strs):
    result = defaultdict(list)

    for string in strs:
        count = [0] * 26

        for char in string:
            count[ord(char) - ord("a")] += 1

        result[tuple(count)].append(string)

    return result.values()
