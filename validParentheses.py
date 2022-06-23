"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid. An input string is valid if:
            1. Open brackets must be closed by the same type of brackets.
            2. Open brackets must be closed in the correct order."""
s1 = '()[{(){}[]}'
def par(s):
    n = len(s)
    sta = []
    if n % 2 != 0:
        return False
    else:
        for i in range(n):
            if s[i] in '{[(':
                sta.append(s[i])
            else:
                if len(sta) == 0:
                    return False
                elif s[i] == '}' and sta.pop() != '{':
                    return False
                elif s[i] == ']' and sta.pop() != '[':
                    return False
                elif s[i] == ')' and sta.pop() != '(':
                    return False

    return len(sta) == 0

print(par(s1))
