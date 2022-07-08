# reverse the sentence but not the words
s = "crulgzfkif gg ombt vemmoxrgf qoddptokkz op xdq hv "

def revWord(w, i, j):
    """reversing a word"""
    w_rev = ''
    for k in range(j, i-1, -1):
        w_rev += w[k]
    return w_rev

def revSentence(A):
    """reversing a sentence"""
    n = len(A)
    rev = revWord(A, 0, n - 1)  # reversed the whole string(including words, but we don't want words to be reversed)
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
    final = final.split()  # try without split function
    ans = ''
    for i in range(len(final)):
        if i != len(final)-1:
            ans += final[i]+' '
        else:
            ans += final[i]
    return ans

    # A = A.split()  # simple 3 lines for the same code
    # A = A[::-1]
    # return ' '.join(A)

print(revSentence(s))
