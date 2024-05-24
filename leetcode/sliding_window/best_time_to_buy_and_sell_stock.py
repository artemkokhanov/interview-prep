from typing import List


def max_profit(prices: List[int]) -> int:
    # left = buy, right = sell
    left, right = 0, 1
    max_p = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_p = max(max_p, profit)
        else:
            left = right
        right += 1

    return max_p
