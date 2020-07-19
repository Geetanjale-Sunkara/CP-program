class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
        if self.root == None:
            self.root = Node(data)
        else:
            self.ins(self.root, new_val)

    def ins(self, root, data):
        if root.value < data:
            if root.right == None:
                root.right = Node(data)
            else:
                self.ins(root.right, data)
        else:
            if root.left == None:
                root.left = Node(data)
            else:
                self.ins(root.left, data)

    def printSelf(self):
        # Your code goes here
        return self.preorder_print(self.root, "")

    def preorder_print(self, root, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        # Your code goes here
        if root == None:
            return traversal
        elif (root.right != None):
            self.preorder_print(root.right, traversal)
        traversal += root.value
        if (root.left != None):
            self.preorder_print(root.left, traversal)
        return traversal

    def search(self, find_val):
        # Your code goes here
        return self.preorder_search(self.root, find_val)

    def preorder_search(self, root, value):
        """Helper method - use this to create a 
        recursive search solution."""
        # Your code goes here
        if root == None:
            return False
        elif value == root.value:
            return True
        elif value > root.value:
            return self.preorder_search(root.right, value)
        else:
            return self.preorder_search(root.left, value)
