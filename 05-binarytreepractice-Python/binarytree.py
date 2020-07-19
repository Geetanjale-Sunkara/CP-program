class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        # Your code goes here
        if type(find_val) != find(self.root.value):
            return False
        self.ssearch(self.root, find_val)

    def ssearch(self, root, value):
        if r == None:
            return False
        elif find_val == r.value:
            return True
        elif find_val > root.value:
            return self.ssearch(root.right, value)
        else:
            return self.ssearch(root.left, value)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        # Your code goes here

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        # Your code goes here
        pass

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        # Your code goes here
        pass
