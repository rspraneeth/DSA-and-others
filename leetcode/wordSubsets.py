from collections import defaultdict

w1 = ["amazon", "apple", "facebook", "google", "leetcode"]
w2 = ["l", "e"]


def wordSubsets1(words1, words2):
    """Bruteforce: Using hashmap and checking frequency, but this makes time complexity very worst"""
    hw1 = []
    for word in words1:
        hm = defaultdict(int)
        for i in word:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1
        hw1.append(hm)

    hw2 = []
    for word in words2:
        hm = defaultdict(int)
        for i in word:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1
        hw2.append(hm)
    ans = []
    l = 0
    for i in hw1:
        flag = True
        for j in hw2:
            for k in j:
                if k not in i:
                    flag = False
                    break
                if j[k] > i[k]:
                    flag = False
                    break

            if not flag:
                break
        if flag:
            ans.append(words1[l])
        l += 1

    return ans


def wordSubsets2(words1, words2):
    """Using new counter function. For each word in words2, we use function counter to count occurrence of each letter.
    We take the maximum occurrences of counts, and use it as a filter of A. Every letter in each word of words1 should
    have frequency <= counts array"""

    def counter(string):
        count_26 = [0] * 26
        for letter in string:
            count_26[ord(letter) - ord('a')] += 1
        return count_26

    count = [0] * 26  # has max frequency of each letter for every word in words2
    for word in words2:
        temp = counter(word)
        for i in range(26):
            count[i] = max(count[i], temp[i])

    ans = []
    for word in words1:
        temp = counter(word)
        for i in range(26):
            if temp[i] < count[i]:  # if freq of each letter is less than freq of words2, it's not universal.
                break
            if i == 25:
                ans.append(word)

    return ans


print(wordSubsets1(w1, w2))
print(wordSubsets2(w1, w2))

# Leet code: 916. Word Subsets
# You are given two string arrays words1 and words2. A string b is a subset of string a if every letter in b
# occurs in a including multiplicity. For example, "wrr" is a subset of "warrior" but is not a subset of "world".
# A string a from words1 is universal if for every string b in words2, b is a subset of a.
# Return an array of all the universal strings in words1. You may return the answer in any order.
