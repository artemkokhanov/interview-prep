from collections import defaultdict
from collections.abc import dict_values
from typing import List, Any


def groupAnagrams(strs: List[str]) -> dict_values[Any, list]:
    result = defaultdict(list)

    for string in strs:
        count = [0] * 26  # a ... z

        for char in string:
            # how does the below work?
            # a = 80 -> 80 - 80 = 0 = a
            # b = 81 -> 81 - 80 = 1 = b
            count[ord(char) - ord("a")] += 1

        result[tuple(count)].append(string)  # tuple because lists cannot be keys in python

    return result.values()  # want the list of strings that match the count key for each string
