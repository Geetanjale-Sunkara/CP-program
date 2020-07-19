"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        # Your code goes here
        h = self.head
        while (h.next != None):
            h = h.next
        h.next = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        i = 0
        h = self.head
        prev = None
        while (i < position):
            prev = h
            h = h.next
            i += 1
        return prev

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        i = 0
        h = self.head
        prev = None
        while (i < position):
            prev = h
            h = h.next
            i += 1
        prev.next = new_element
        new_element.next = h

    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        h = self.head
        prev = None
        while h.value != value:
            prev = h
            h = h.next
        if (prev == None):
            self.head = h.next
        else:
            prev.next = h.next
        return h
