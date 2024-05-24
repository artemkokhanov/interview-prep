def reverse_number(num):
    reverse = str(num)[::-1]
    return reverse


print(reverse_number(1223))


def reverse_number_solution(num):
    num_str = str(num)
    num_list = list(num_str)

    left, right = 0, len(num_list) - 1

    while left < right:
        num_list[left], num_list[right] = num_list[right], num_list[left]
        left += 1
        right -= 1

    return int(''.join([x for x in num_list]))


print(reverse_number_solution(123))
print(reverse_number_solution(1))
print(reverse_number_solution(987654321))
