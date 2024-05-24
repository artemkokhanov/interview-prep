# https://leetcode.com/problems/reverse-string/description/

def reverse_string(s: str) -> str:
    str_list = list(s)

    left, right = 0, len(s) - 1

    while left < right:
        str_list[left], str_list[right] = str_list[right], str_list[left]
        left += 1
        right -= 1

    return ''.join(str_list)


def reverse_string_oneliner(s: str) -> None:
    s[:] = s[::-1]


test_string = "Hello, World!"
reversed_test_string = reverse_string(test_string)
print(reversed_test_string)
