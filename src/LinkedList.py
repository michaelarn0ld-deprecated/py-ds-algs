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

        """
        1->2->3->None
        current = 1->2->3->none
        next = 2->3->none
        current.next = none
        previous = 1->none
        currrent = 2->3->none


        1->none 2->3->none
        current = 2->3->none
        next  = 3->none
        current.next = previous = 1->none
        previous = 2->1->none
        current = 3->none

        2->1->none 3->None
        current = 3->none
        next = none
        current.next = previous = 2->1->none
        previous = 3->2->1->none
        current = none
        """

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