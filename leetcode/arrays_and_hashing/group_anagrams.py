from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    result = defaultdict(list)

    for string in strs:
        count = [0] * 26

        for char in string:
            count[ord(char) - ord("a")] += 1

        result[tuple(count)].append(string)

    return result.values()
