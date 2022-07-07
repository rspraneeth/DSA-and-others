# reverse the sentence but not the words
s = 'mailman bring letters'

def revWord(w, i, j):
    """reversing a word"""
    w_rev = ''
    for k in range(j, i-1, -1):
        w_rev += w[k]
    return w_rev

def revSentence(a):
    """reversing a sentence"""
    n = len(a)
    rev = revWord(a, 0, n-1)  # reversed the whole string(including words, but we don't want words to be reversed)
    l, r = 0, 0
    final = ''
    for i in range(len(rev)):  # reversing the reversed words
        if rev[i] == ' ' or i == len(rev)-1:  # using 2 pointer l, r
            if i == len(rev)-1:
                r = i
                b = revWord(rev, l, r)
            else:
                r = i-1
                b = revWord(rev, l, r)
                b += ' '
            final += b
            l = i+1
            r = i+1
        else:
            r += 1

    return final

print(revSentence(s))
