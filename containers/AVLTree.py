from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    def __init__(self, xs=None):
        super().__init__()

    def balance_factor(self):
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        return AVLTree._is_avl_satisfied(self.root)

    def _is_avl_satisfied(node):
        if not node:
            return True
        ret = False
        if AVLTree._balance_factor(node) in [-1, 0, 1]:
            ret = True
        if node.left:
            ret &= AVLTree._is_avl_satisfied(node.left)
        if node.right:
            ret &= AVLTree._is_avl_satisfied(node.right)
        return ret

    @staticmethod
    def _left_rotate(node):
        og_root = node.value
        new_root = node.right
        node.value = node.right.value
        og_root_right = node.right.left
        og_root_left = node.left
        node.value = new_root.value
        node.right = new_root.right
        node.left = Node(og_root, og_root_left, og_root_right)
        return node

    @staticmethod
    def _right_rotate(node):
        og_root = node.value
        new_root = node.left
        node.value = node.left.value
        og_root_right = node.right
        og_root_left = node.left.right
        node.value = new_root.value
        node.left = new_root.left
        node.right = Node(og_root, og_root_left, og_root_right)
        return node

    @staticmethod
    def _rebalance(node):
        if node == None: 
            return 
        if AVLTree._balance_factor(node) <= -2: 
            if AVLTree._balance_factor(node.right) > 0:
                AVLTree._right_rotate(node.right)
                AVLTree._left_rotate(node)
            else:
                AVLTree._left_rotate(node)
        if AVLTree._balance_factor(node) >= 2: 
            if AVLTree._balance_factor(node.right) < 0:
                AVLTree._left_rotate(node.left)
                AVLTree._right_rotate(node)
            else:
                AVLTree._right_rotate(node)
        if node.left:
            AVLTree._rebalance(node.left)
        if node.right: 
            AVLTree._rebalance(node.right) 

    def insert(self, value):
        if self.root:
            AVLTree._insert(self.root, value)
            AVLTree._rebalance(self.root)
            #replace with BST._insert
            #AVLTree._rebalance(node)
        else:
            self.root = Node(value)
        

    @staticmethod
    def _insert(node, value): 
        if not node:
            node.value = Node(value)
        if value < node.value:
            if node.left:
                AVLTree._insert(node.left, value)
            else:
                node.left = Node(value)
        if value > node.value:
            if node.right:
                AVLTree._insert(node.right, value)
            else:
                node.right = Node(value)
        AVLTree._rebalance(node)

    def insert_list(self, xs): 
        if len(xs) != 0:
            for num in xs: 
                self.insert(num)
