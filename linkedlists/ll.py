class Node:
    """Node class"""
    def __init__(self, data):
        """Function to initialize the Node object"""
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

class LinkedList:
    """Linked List class"""
    def __init__(self):
        """Function to initialize the LinkedList object"""
        self.head = None
        self.length = 0

    def insert_node(self, position, value):
        """Function to insert a new node at a given position. To insert new node at kth position,
        We go to (k-1)th node/previous node and reference new node with previous nodes reference
        and reference previous node with new node. Here in the code, cur is previous node"""
        new = Node(value)
        if position > self.length + 1:  # at max, we can insert at last position i.e. (length+1)position.
            print(f"Insertion not possible at given position {position}. As current length of linked list is {self.length}, we can only insert till {self.length+1}nd position.")
            return
        if position == 1:  # insertion at first position
            new.next = self.head  # the head has address of 1st node. So, new node references to value in head
            self.head = new  # now head references to new, so new becomes 1st noe
            self.length += 1  # we increment length for any insertion
        else:  # for insertion at any other position or last position
            cur = self.head  # with 1st node
            cur_pos = 1  # since we are with 1st node, current_position = 1
            while cur_pos < position - 1:  # we are going till previous node of position
                cur = cur.next
                cur_pos += 1
            new.next = cur.next  # new node reference will be previous nodes reference
            cur.next = new  # previous node references to new node
            self.length += 1  # we increment length for any insertion

    def delete_node(self, position):
        """Function to delete a node at given position. To delete a node at kth position,
        We go to (k-1)th node/previous node and change the address to next next node"""
        if position > self.length:  # can't delete a node that doesn't exist
            print(f"No element exist at given position {position} to delete.")
            return
        cur = self.head
        if position == 1:  # deleting node at 1st position
            self.head = cur.next
            self.length -= 1
        else:
            cur_pos = 1
            while cur_pos < position - 1:
                cur = cur.next
                cur_pos += 1
            cur.next = cur.next.next
            self.length -= 1

    def print_ll(self):
        # Output each element followed by a space
        cur = self.head
        if cur is None:
            print(None)
        else:
            while cur.next is not None:
                print(cur.data, end=' ')
                cur = cur.next
            print(cur.data)

if __name__ == '__main__':
    ll = LinkedList()  # creating a new linked list object
    ll.insert_node(1, 1)  # calling functions
    ll.print_ll()
    ll.insert_node(3, 2)
    ll.print_ll()
    for i in range(2, 11):
        ll.insert_node(i, i)
    ll.print_ll()
    ll.delete_node(5)
    ll.print_ll()
    ll.delete_node(10)
