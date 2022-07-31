w = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
p = "abb"

def findAndReplacePattern1(words, pattern):
    """Approach: We normalise a string to a particular pattern, Eg:'aab' is '001', 'qqf' is '001', 'qfq' is '010'.
     aab matches with qqf."""
    def normalise(string):
        word_list = []
        num_list = []
        for k in string:
            if k in word_list:
                num_list.append(word_list.index(k))
            else:
                word_list.append(k)
                num_list.append(word_list.index(k))
        return num_list

    ans = []
    plist = normalise(pattern)
    for word in words:
        wlist = normalise(word)
        if wlist == plist:
            ans.append(word)

    return ans

def findAndReplacePattern2(words, pattern):
    """Same as previous approach, but using python to best. setdefault function returns the value of a key if present,
    else it sets the value of a key as 2nd parameter passed"""
    def normalise(string):
        m = {}
        return [m.setdefault(k, len(m)) for k in string]

    pl = normalise(pattern)
    return [word for word in words if normalise(word) == pl]

print(findAndReplacePattern1(w, p))
print(findAndReplacePattern1(w, p))

# Leet code: 890. Find and Replace Pattern
# Given a list of strings words and a string pattern, return a list of words[i] that match pattern.
# You may return the answer in any order. A word matches the pattern if there exists a permutation of letters p
# so that after replacing every letter x in the pattern with p(x), we get the desired word.
# Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter,
# and no two letters map to the same letter.
