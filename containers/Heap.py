'''
This file implements the Heap data structure as a subclass of the BinaryTree.
The book implements Heaps using an *implicit* tree with an *explicit* vector implementation,
so the code in the book is likely to be less helpful than the code for the other data structures.
The book's implementation is the traditional implementation because it has a faster constant factor
(but the same asymptotics).
This homework is using an explicit tree implementation to help you get more practice with OOP-style programming and classes.
'''

from containers.BinaryTree import BinaryTree, Node


class Heap(BinaryTree):

    def __init__(self, xs=None):
        self.root = None
        if xs is not None:
            Heap.insert_list(self, xs)

    def __repr__(self):
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        if len(self) == 1:
            return True
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        ret = True
        if node.left:
            ret &= node.value <= node.left.value
            ret &= Heap._is_heap_satisfied(node.left)
        if node.right:
            ret &= node.value <= node.right.value
            ret &= Heap._is_heap_satisfied(node.right)
        return ret

    def insert(self, value):
        self.num_nodes = 1 + len(self)
        binary_str = bin(self.num_nodes)[3:]
        if self.root:
            Heap._insert(self.root, value, binary_str)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(node, value, binary_str):
        if binary_str[0] == '0':
            if len(binary_str) == 1:
                node.left = Node(value)
            else:
                Heap._insert(node.left, value, binary_str[1:])
            if node.value > node.left.value:
                node.value, node.left.value = node.left.value, node.value
        if binary_str[0] == '1':
            if len(binary_str) == 1:
                node.right = Node(value)
            else:
                Heap._insert(node.right, value, binary_str[1:])
            if node.value > node.right.value:
                node.value, node.right.value = node.right.value, node.value

    def insert_list(self, xs):
        for num in xs:
            Heap.insert(self, num)

    def find_smallest(self):
        return self.root.value

    def remove_min(self):
        if len(self) == 0:
            return
        if len(self) == 1:
            self.root = None
            return
        self.num_nodes = len(self)
        binary_str = bin(self.num_nodes)[3:]
        self.root.value = Heap._remove_bottom_right(self.root, binary_str)
        Heap._trickle_down(self.root)
        '''
        Removes the minimum value from the Heap.
        If the heap is empty, it does nothing.

        FIXME:
        Implement this function.

        HINT:
        The pseudocode is
        1. remove the bottom right node from the tree
        2. replace the root node with what was formerly the bottom right
        3. "trickle down" the root node: recursively swap it with its largest child until the heap property is satisfied

        '''
        
    @staticmethod
    def _remove_bottom_right(node, binary_str):
        if binary_str[0] == '0':
            if len(binary_str) == 1:
                remove_bottom = node.left.value
                node.left = None
                return remove_bottom
            else:
                return Heap._remove_bottom_right(node.left, binary_str[1:])
        elif binary_str[0] == '1':
            if len(binary_str) == 1:
                remove_bottom = node.right.value
                node.right = None
                return remove_bottom
            else:
                return Heap._remove_bottom_right(node.right, binary_str[1:])

    @staticmethod
    def _trickle_down(node):
        print("trickle_down activated")
        if node.right is not None and node.left is not None:
            if node.right.value >= node.left.value:
                print("node.right.value:", node.right.value, ">= node.left.value", node.left.value)
                if node.value >= node.right.value or node.value >= node.left.value:
                    node.value, node.left.value = node.left.value, node.value
                    print("swapped node and left")
            elif node.left.value > node.right.value:
                if node.value >= node.left.value or node.value > node.right.value:
                    node.value, node.right.value = node.right.value, node.value
            Heap._trickle_down(node.left)
            Heap._trickle_down(node.right)
        elif node.right is not None:
            if node.value > node.right.value:
                #swap with right
                node.value, node.right.value = node.right.value, node.value
            Heap._trickle_down(node.right)
        elif node.left is not None:
            if node.value > node.left.value:
                node.value, node.left.value = node.left.value, node.value
            Heap._trickle_down(node.left)
