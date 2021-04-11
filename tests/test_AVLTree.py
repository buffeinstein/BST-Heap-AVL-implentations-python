from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST
from containers.AVLTree import AVLTree

################################################################################
# these tests are specific for AVLTree rotations

avltree0 = AVLTree()
avltree0.root = Node(5)
avltree0.root.left = Node(3)
avltree0.root.left.left = Node(1)
avltree0.root.right = Node(7)

avltree1 = AVLTree()
avltree1.root = Node(5)
avltree1.root.left = Node(3)
avltree1.root.left.right = Node(4)
avltree1.root.right = Node(7)

avltree2 = AVLTree()
avltree2.root = Node(5)
avltree2.root.left = Node(3)
avltree2.root.right = Node(7)
avltree2.root.right.left = Node(6)

avltree3 = AVLTree()
avltree3.root = Node(5)
avltree3.root.left = Node(3)
avltree3.root.right = Node(7)
avltree3.root.right.right = Node(9)

avltree4 = AVLTree()
avltree4.root = Node(5)
avltree4.root.left = Node(3)
avltree4.root.left.left = Node(1)
avltree4.root.left.right = Node(4)
avltree4.root.right = Node(7)
avltree4.root.right.left = Node(6)
avltree4.root.right.right = Node(9)

'''
NOTE:
An important property of tree rotations is that they maintain the BST property.
This implies that an inorder traversal of the pre-rotated and post-rotated trees will be the same:
they will both be sorted lists.
This is the ONLY property of tree rotations being tested in these test cases,
and so passing these test cases does not 100% guarantee that your tree rotations are correct.
In particular, passing these test cases is a necessary but not a sufficient condition for correct rotation implementations.
'''

def test__AVLTree__left_rotate0():
    rotated = AVLTree()
    rotated.root = AVLTree._left_rotate(avltree0.root)
    assert rotated.is_bst_satisfied()
    assert rotated.to_list('inorder') == avltree0.to_list('inorder')

def test__AVLTree__left_rotate1():
    rotated = AVLTree()
    rotated.root = AVLTree._left_rotate(avltree1.root)
    assert rotated.is_bst_satisfied()
    assert rotated.to_list('inorder') == avltree1.to_list('inorder')

def test__AVLTree__left_rotate4():
    rotated = AVLTree()
    rotated.root = AVLTree._left_rotate(avltree4.root)
    assert rotated.is_bst_satisfied()
    assert rotated.to_list('inorder') == avltree4.to_list('inorder')

def test__AVLTree__right_rotate2():
    rotated = AVLTree()
    rotated.root = AVLTree._right_rotate(avltree2.root)
    assert rotated.is_bst_satisfied()
    assert rotated.to_list('inorder') == avltree2.to_list('inorder')

def test__AVLTree__right_rotate3():
    rotated = AVLTree()
    rotated.root = AVLTree._right_rotate(avltree3.root)
    assert rotated.is_bst_satisfied()
    assert rotated.to_list('inorder') == avltree3.to_list('inorder')

def test__AVLTree__right_rotate4():
    rotated = AVLTree()
    rotated.root = AVLTree._right_rotate(avltree4.root)
    assert rotated.is_bst_satisfied()
    assert rotated.to_list('inorder') == avltree4.to_list('inorder')


################################################################################
# These tests are all copied from the BST tests

def test__AVLTree_super():
    x = AVLTree()
    assert isinstance(x,BinaryTree)
    assert isinstance(x,BST)


def test__AVLTree_is_avl_satisified0a():
    avl = AVLTree()
    avl.root = Node(0)
    avl.root.left = Node(-1)
    assert avl.is_bst_satisfied()
    assert avl.is_avl_satisfied()

def test__AVLTree_is_avl_satisified0b():
    avl = AVLTree()
    avl.root = Node(0)
    assert avl.is_bst_satisfied()
    assert avl.is_avl_satisfied()

def test__AVLTree_is_avl_satisified0():
    avl = AVLTree()
    avl.root = Node(0)
    avl.root.left = Node(-1)
    avl.root.left.left = Node(-2)
    assert avl.is_bst_satisfied()
    assert not avl.is_avl_satisfied()

def test__AVLTree_is_avl_satisified1():
    avl = AVLTree()
    avl.root = Node(0)
    avl.root.right = Node(1)
    avl.root.right.right = Node(2)
    assert avl.is_bst_satisfied()
    assert not avl.is_avl_satisfied()

def test__AVLTree_is_avl_satisified2():
    avl = AVLTree()
    avl.root = Node(0)
    avl.root.right = Node(1)
    avl.root.right.right = Node(2)
    assert avl.is_bst_satisfied()
    assert not avl.is_avl_satisfied()

def test__AVLTree_is_avl_satisified3():
    avl = AVLTree()
    avl.root = Node(0)
    avl.root.right = Node(1)
    avl.root.right.right = Node(2)
    avl.root.right.right.right = Node(3)
    avl.root.left = Node(-1)
    assert avl.is_bst_satisfied()
    assert not avl.is_avl_satisfied()

def test__AVLTree_is_avl_satisified4():
    avl = AVLTree()
    assert avl.is_bst_satisfied()
    assert avl.is_avl_satisfied()

def test__AVLTree_is_avl_satisified5():
    avl = AVLTree()
    avl.root = Node(0)
    assert avl.is_bst_satisfied()
    assert avl.is_avl_satisfied()

def test__AVLTree_is_avl_satisified6():
    avl = AVLTree()
    avl.root = Node(0)
    avl.root.right = Node(1)
    assert avl.is_bst_satisfied()
    assert avl.is_avl_satisfied()

def test__AVLTree_is_avl_satisified7():
    avl = AVLTree()
    avl.root = Node(0)
    avl.root.left = Node(-2)
    avl.root.left.left = Node(-3)
    avl.root.left.right = Node(-1)
    avl.root.right = Node(1)
    assert avl.is_bst_satisfied()
    assert avl.is_avl_satisfied()

def test__AVLTree_is_avl_satisified8():
    avl = AVLTree()
    avl.root = Node(0)
    avl.root.left = Node(-2)
    avl.root.left.left = Node(-3)
    avl.root.left.left.left = Node(-4)
    avl.root.left.right = Node(-1)
    avl.root.right = Node(2)
    avl.root.right.left = Node(1)
    avl.root.right.right = Node(3)
    avl.root.right.right.right = Node(4)
    avl.root.right.right.right.right = Node(5)
    assert avl.is_bst_satisfied()
    assert not avl.is_avl_satisfied()

def test__AVLTree_is_avl_satisified9():
    avl = AVLTree()
    avl.root = Node(0)
    avl.root.left = Node(-2)
    avl.root.left.left = Node(-3)
    avl.root.left.left.left = Node(-4)
    avl.root.left.left.left.left = Node(-5)
    avl.root.left.right = Node(-1)
    avl.root.right = Node(2)
    avl.root.right.left = Node(1)
    avl.root.right.right = Node(3)
    avl.root.right.right.right = Node(4)
    assert avl.is_bst_satisfied()
    assert not avl.is_avl_satisfied()

################################################################################

import random
import copy
from hypothesis import given
import hypothesis.strategies as st
ints = st.lists(st.integers())


@given(xs=ints)
def test__AVLTree_insert(xs):
    xs = list(set(xs))
    avl = AVLTree()
    for x in xs:
        avl.insert(x)
        assert x in avl.to_list('inorder')
        assert avl.is_bst_satisfied()
        assert avl.is_avl_satisfied()
    

@given(xs=ints)
def test__AVLTree_insert_list(xs):
    xs = list(set(xs))
    avl = AVLTree()
    avl.insert_list(xs)
    assert avl.is_bst_satisfied()
    assert avl.is_avl_satisfied()
    

@given(xs=ints)
def test__AVLTree___init__(xs):
    xs = list(set(xs))
    avl = AVLTree(xs)
    assert avl.is_bst_satisfied()
    assert avl.is_avl_satisfied()


# NOTE: 
# We are NOT testing the following functions: 
#   __contains__
#   find
#   find_smallest
#   find_largest
# These functions all get inherited from the BST class,
# and since every valid AVLTree is also a valid BST,
# we know that these functions are guaranteed to continue working.

# NOTE:
# I am not having you implement the remove function,
# and therefore the following test cases are commented out.
"""
@given(xs=ints)
def test__AVLTree_remove1(xs):
    '''
    This tests the remove function.
    In order to test the remove function, we must be able to generate valid AVLTrees.
    Therefore, you must have all the insert functionality completed before this test can pass.
    '''
    random.seed(0)
    xs = list(set(xs))
    avl = AVLTree(xs)
    while len(xs)>0:
        x = random.choice(xs)
        xs.remove(x)
        assert x in avl
        avl.remove(x)
        assert x not in avl
        assert set(avl.to_list('inorder'))==set(xs)
        assert avl.is_avl_satisfied()


@given(xs=ints)
def test__AVLTree_remove2(xs):
    '''
    If we remove something from the AVLTree that is not in the AVLTree,
    then the AVLTree should remain unchanged.
    '''
    xs = list(set(xs))
    avl = AVLTree(xs)
    y = 0
    while y in xs:
        y += 1
    avl.remove(y)
    assert avl.to_list('inorder')==sorted(xs)


@given(xs=ints, ys=ints)
def test__AVLTree_remove_list(xs,ys):
    xs = list(set(xs))
    avl = AVLTree(xs)
    avl.remove_list(ys)
    for y in ys:
        assert y not in avl
"""

@given(xs=ints)
def test__AVLTree_inorder_property(xs):
    '''
    The order we insert objects into a AVLTree can affect the structure of the tree,
    but it should NOT affect the list we get out from an inorder traversal.
    (Recall that the inorder traversal of a AVLTree should always be a sorted list.)
    This test randomly shuffles the input list two different ways
    and checks that both shufflings give the same output list.
    This tests both the insertion functions and the traversal functions
    to ensure that there are no bad interactions between theses functions.
    '''
    xs = list(set(xs))
    random.seed(0)

    xs1 = copy.copy(xs)
    random.shuffle(xs1)
    bst1 = AVLTree(xs1)

    xs2 = copy.copy(xs)
    random.shuffle(xs2)
    bst2 = AVLTree(xs2)
    
    assert bst1.to_list('inorder') == bst2.to_list('inorder')


@given(xs=ints)
def test__AVLTree_eq(xs):
    '''
    This test is essentially the same as the previous one,
    but tests the == operator specifically.
    '''
    xs = list(set(xs))

    xs1 = copy.copy(xs)
    random.shuffle(xs1)
    bst1 = AVLTree(xs1)

    xs2 = copy.copy(xs)
    random.shuffle(xs2)
    bst2 = AVLTree(xs2)

    assert bst1 == bst2
