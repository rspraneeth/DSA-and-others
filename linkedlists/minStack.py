# find the min value in the stack, Approach: with 2 stacks, one for elements and one for min values
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.minhead = None

    def push(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

        if self.minhead is None:
            self.minhead = Node(x)
        elif x < self.minhead.val:
            mnew = Node(x)
            mnew.next = self.minhead
            self.minhead = mnew

    def pop(self):
        if self.head is None:
            return
        if self.head.val == self.minhead.val:
            self.minhead = self.minhead.next
        self.head = self.head.next

    def top(self):
        if self.head:
            return self.head.val
        else:
            return -1

    def getMin(self):
        if self.minhead:
            return self.minhead.val
        else:
            return -1

    def print_ll(self):
        cur = self.head
        if cur is None:
            print(None)
        else:
            while cur.next is not None:
                print(cur.val, end=' ')
                cur = cur.next
            print(cur.val)

ll = LinkedList()
ll.push(-11)
ll.push(2)
ll.push(-12)
ll.pop()
ll.print_ll()
print(ll.getMin())
