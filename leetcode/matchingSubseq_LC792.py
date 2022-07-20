s1 = "dsahjpjauf"
words1 = ["ahjpjau", "ja", "ahbwzgqnuk", "nanowatt"]

def numMatchingSubseq(s, words):
    """we calculate by checking each word in array with given string, and using hashmap for repetitive words"""
    b = {}  # converting list to dict, so that for repeated words in list, we need not iterate again
    for i in words:
        b[i] = b.get(i, 0) + 1
    words = b

    count = 0
    for word in words:  # increasing count when they match by value of the key (freq of word)
        j, k = 0, 0
        while j < len(word) and k < len(s):
            if word[j] == s[k]:
                j += 1
                k += 1
            else:
                k += 1
        if j == len(word):  # means reached end of the word
            count += words.get(word)

    return count

print(numMatchingSubseq(s1, words1))

# Leet code 792. Number of Matching Subsequences
# Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.
# A subsequence of a string is a new string generated from the original string with some characters (can be none)
# deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
