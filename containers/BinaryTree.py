'''
This file implements the Node and BinaryTree classes.
These two classes are the building blocks for the BST, AVLTree, and Heap data structures.
It is crucial to get these implemented correctly in order to be able to implement the other data structures.
'''


class Node():
    '''
    You do not have to implement anything within this class.
    Given a node t, you can visualize the node by running str(t) in the python interpreter.
    This is a key method to perform debugging,
    so you should get familiar with how to visualize these strings.
    '''

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left    # NOTE: left should always be a Node
        self.right = right  # NOTE: right should always be a Node

    def __str__(self):
        ret = '('
        ret += str(self.value)
        ret += ' - '
        if self.left:
            ret += str(self.left)
            ret += ' '
        ret += '- '
        if self.right:
            ret += str(self.right)
            ret += ' '
        ret += ')'
        return ret


class BinaryTree():
    '''
    This class is relatively useless by itself,
    but it is the superclass for the BST, AVLTree, and Heap classes,
    and it provides important helper functions for these classes.
    If you don't implement all of the functions in this class correctly,
    it will be impossible to implement those other classes.
    '''

    def __init__(self, root=None):
        '''
        Construct a BinaryTree, possibly with a single element in it.
        Note that for an ordinary BinaryTree, we cannot insert more than one element in the constructor,
        but for the BST (and other tree types) we can.
        '''
        if root:
            self.root = Node(root)
        else:
            self.root = None

    def __str__(self):
        '''
        We can visualize a tree by visualizing its root node.
        '''
        return str(self.root)

    def print_tree(self, traversal_type):
        '''
        There are three primary types of tree traversals: preorder, inorder, and postorder.
        All three of these traversals are implemented for you as a reference on how to write recursive functions on recursive data structures.
        '''
        if traversal_type == 'preorder':
            return self.preorder_print(self.root, '')
        elif traversal_type == 'inorder':
            return self.inorder_print(self.root, '')
        elif traversal_type == 'postorder':
            return self.postorder_print(self.root, '')
        else:
            raise ValueError('Traversal type ' + str(traversal_type) + ' is not supported.')

    def preorder_print(self, start, traversal):
        '''
        Prints the nodes using a preorder traversal.
        '''
        if start:
            traversal += str(start.value) + '-'
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        '''
        Prints the nodes using a inorder traversal.
        '''
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += str(start.value) + '-'
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        '''
        Prints the nodes using a postorder traversal.
        '''
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += str(start.value) + '-'
        return traversal

    def to_list(self, traversal_type):
        '''
        This function is similar to the print_tree function,
        but instead of printing the tree,
        it returns the contents of the tree as a list.

        A general programming principle is that a function should return its results
        rather than print them whenever possible.
        If a function returns its results,
        we can always print the returned results if we need to visualize them.
        But by returning the results we can also do more computations on the results if needed.
        Many of the test cases for more complicated tree functions rely on this to_list function,
        so it is import to implement it correctly.

        FIXME:
        Implement this function by modifying the _print functions above.
        '''

    def preorder(self, start, traversal):
        '''
        FIXME:
        Implement this function by modifying the _print functions above.
        '''

    def inorder(self, start, traversal):
        '''
        FIXME:
        Implement this function by modifying the _print functions above.
        '''

    def postorder(self, start, traversal):
        '''
        FIXME:
        Implement this function by modifying the _print functions above.
        '''

    def __len__(self):
        '''
        Returns the number of elements contained in the tree.
        Recall that `tree.__len__()` will desugar to `size(len)`.
        '''
        return BinaryTree.__len__helper(self.root)

    @staticmethod
    def __len__helper(node):
        '''
        FIXME:
        Implement this function.

        HINT:
        The pseudocode is:
        add 1 for the current node;
        if a left child exists, add the result of __len__helper on the left child;
        if a right child exists, add the result of __len__helper on the right child;
        return the sum of these three steps
        '''

    def height(self):
        '''
        Returns the height of the tree.
        Recall that the height is the maximum length from the root to a leaf node.

        FIXME:
        Implement this function.

        HINT:
        See how the __len__ method calls its helper staticmethod.
        '''

    @staticmethod
    def _height(node):
        '''
        FIXME:
        Implement this function.

        HINT:
        The pseudocode is:
        if a left child exists, calculate the _height of the left child;
        if a right child exists, calculate the _height of the right child;
        return 1 (for the current node) plus the max of the left and right _heights calculated above
        '''
