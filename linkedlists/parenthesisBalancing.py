class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def __init__(self):
        self.head = None
        self.c = 0  # to keep track of parenthesis pair, == 0 means there is no parenthesis unclosed

    def solve(self, A):
        """Using stack linkedlist"""
        for i in A:
            if self.head is None and i in '}])':
                return 0
            if i in '{[(':
                new = Node(i)
                new.next = self.head
                self.head = new
            elif (i == '}' and self.head.val == '{') or (i == ']' and self.head.val == '[') or (i == ')' and self.head.val == '('):
                self.head = self.head.next
        if self.head:
            return 0
        return 1

    def solve1(self, A):
        """Normal approach without stack linkedlist"""
        l = []
        for i in A:
            if self.c == 0 and i in '}])':
                return 0
            if i in '{[(':
                l.append(i)
                self.c += 1
            elif (i == ']' and l[-1] == '[') or (i == '}' and l[-1] == '{') or (i == ')' and l[-1] == '('):
                self.c -= 1
                l = l[:-1]
        return (0, 1)[self.c == 0]

if __name__ == '__main__':
    s = Solution()
    print(s.solve('{([])}{}'))
    print(s.solve1('{([])}{'))
