# Driver code for the linked list type data structure
# Linked List class contains function to reverse the linked list

# ----------------------------------------------
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__ (self,head=None):
        self.head = None

    def reverse(self):
        current = self.head
        previous = None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def printList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
# ----------------------------------------------

# Sample implementation of the linked list
llist = LinkedList()
for i in range(6):
    if not llist.head:
        llist.head = Node(i)
        current = llist.head
    else:
        current.next = Node(i)
        current = current.next

llist.printList()
print('----')
llist.reverse()
llist.printList()