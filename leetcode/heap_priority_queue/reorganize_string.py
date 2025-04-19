import heapq
from collections import Counter


# let n be the length of the input string and k be the number of unique characters in the input string
def reorganizeString(s: str) -> str:
    count = Counter(s)  # Hashmap, count each char, runs in O(n) time
    maxHeap = [[-count, char] for char, count in count.items()]  # data structure to use heapify on, runs in O(k) time
    heapq.heapify(maxHeap)  # runs in O(k) time

    prev = None
    res = ""

    while maxHeap or prev:  # runs in O(n log(k)) time
        if prev and not maxHeap:
            return ""

        # most frequent, except prev
        count, char = heapq.heappop(maxHeap)  # runs in O(log(k)) time
        res += char
        count += 1

        if prev:
            heapq.heappush(maxHeap, prev)  # runs in O(log(k)) time
            prev = None

        if count != 0:
            prev = [count, char]
    return res
