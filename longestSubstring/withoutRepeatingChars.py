def lengthOfLongestSubstring(s):
    """ Approach:
    1. We take an empty list(css[]) to store final/current substring,
    2. we iterate the string(s),
    3. when char is not in css[] -> add char to css[] and increment lss,
    4. when char in css[] -> find ans(max(ans, lss)),
        1. find(index) where the repeated element is in css[] and
        2. start css[] from that index+1 and add the repeated element(char) to css[],
        3. now lss becomes lss-ind (take some time to understand this with example's).
    5. Check if iteration reached final, if final, check for max again(because when s[n-1] not in css[]
       it doesn't go to else condition and the ans will be previous substring length). """
    # eg: 'pwwkew',
    # 1. initially css = [p,w], lss = 2,
    # 2. when repeated element 'w' comes, ans = 2, ind = 1, css = [],after adding repeated element css = [w], lss = 2-1=1,
    # 3. now css = [w,k,e], lss = 3
    # 4. now repeated element 'w' comes, ans = 3, ind = 0, css = [k, e], after adding repeated element css = [k,e,w], lss = 3-0=3,
    # 5. now when reached last element we check ans again i.e., 3

    n = len(s)
    lss = 0  # length of current substring
    css = []  # current substring
    ans = 0  # length of final substring
    for i in range(n):
        if s[i] not in css:
            css.append(s[i])
            lss += 1
        else:
            ans = max(ans, lss)
            ind = css.index(s[i])  # index of repeated char
            css = css[ind + 1:]  # changing list css[] with new substring (removing chars until repeated char)
            css.append(s[i])  # adding repeated char to css[]
            lss = lss - ind  # new current length of substring
        if i == n - 1:  # when final char
            ans = max(ans, lss)
    return ans

print(lengthOfLongestSubstring("abcabcbb"))
