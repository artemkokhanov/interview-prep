def longest_palindrome(s: str) -> str:
    res = ''
    res_length = 0

    for i in range(len(s)):
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > res_length:
                res = s[left:right + 1]
                res_length = right - left + 1
            left -= 1
            right += 1

        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > res_length:
                res = s[left:right + 1]
                res_length = right - left + 1
            left -= 1
            right += 1

    return res
