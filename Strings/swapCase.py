s = 'aHsqLwGcjs'


def swapCase(a):
    new = ''
    for i in a:
        # if i >= 'A' and i <= 'Z':
        #     new += chr(ord(i) + 32)  # 'a'-'A' is 32
        # if i >= 'a' and i <= 'z':
        #     new += chr(ord(i) - 32)
        new += chr(ord(i) ^ 32)
    return new

print(swapCase(s))
