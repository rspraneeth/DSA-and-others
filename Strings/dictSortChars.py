# given a string, sort them on dictionary order
s = 'kjdfncdekjnaaaanjzzzyy'

def dictSort(a):
    """We are storing number of times an alphabet occurs in the given string in to a new array. """
    b = [0]*26  # frequency of char[a-z] is stored in array w.r.t the dictionary order
    for i in a:
        ind = ord(i)-ord('a')  # ord(a) = 65, if i=a, ind = 0, i.e., b[0] stores frequency of 'a', b[25]=freq('z')
        b[ind] += 1
    a = ''
    for i in range(len(b)):
        for j in range(b[i]):
            a += chr(97+i)  # 97 is ascii of 'a', adding 97 to i gives char of i'th index in b[].

    return a

print(dictSort(s))
