def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res


def decode(str):
    res = []
    i = 0

    while i < len(str):  # iterating through each character, decoding string into strings
        j = i
        while str[j] != "#":
            j += 1
        length = int(str[i: j])
        res.append(str[j + 1: j + 1 + length])  # j + 1 because j is the delimiter character
        i = j + 1 + length
    return res
