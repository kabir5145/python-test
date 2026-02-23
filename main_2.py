# Q 1 - sWAP cASE
# def swap_case(s):
#     return s.swapcase()
#
# if __name__ == '__main__':
#     s = input()
#     swap_case(s)
#     result = swap_case(s)
#     print(result)

def swap_case(s):
    result = ""
    for ch in s:
        if ch.islower():
            result += ch.upper()
        elif ch.isupper():
            result += ch.lower()
        else:
            result += ch
    return result

if __name__ == '__main__':
    s = input()
    print(swap_case(s))