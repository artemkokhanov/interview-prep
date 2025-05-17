def longest_palindrome(s: str) -> str:
    res = ''
    res_length = 0

    # Time Complexity: O(n^2) because for each character in the string, we expand left and right for that character, so n * n which is n^2)
    for i in range(len(s)):
        # for odd length palindromes (odd because we take one character and expand to the left and right which will always give us an odd length):
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > res_length:
                res = s[left:right + 1]
                res_length = right - left + 1
            left -= 1
            right += 1

        # for even length palindromes:
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > res_length:
                res = s[left:right + 1]
                res_length = right - left + 1
            left -= 1
            right += 1

    return res
