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
        if type(find_val) != type(self.root.value):
            return False
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        # Your code goes here
        return self.preorder_print(self.root, "")

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
