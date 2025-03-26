import heapq
from collections import Counter


def reorganizeString(s: str) -> str:
    count = Counter(s)  # Hashmap, count each char
    maxHeap = [[-count, char] for char, count in count.items()]  # data structure to use heapify on
    heapq.heapify(maxHeap)  # runs in O(n) time

    prev = None
    res = ""

    while maxHeap or prev:
        if prev and not maxHeap:
            return ""

        # most frequent, except prev
        count, char = heapq.heappop(maxHeap)
        res += char
        count += 1

        if prev:
            heapq.heappush(maxHeap, prev)
            prev = None

        if count != 0:
            prev = [count, char]
    return res
