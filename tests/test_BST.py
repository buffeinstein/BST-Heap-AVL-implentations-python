from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


def test__BST_super():
    x = BST()
    assert isinstance(x,BinaryTree)


# the very first thing to do whenever creating a data structure 
# is to write a function to check if the invariant holds 
# (in this case the BST property)
# and create test cases for whether that function works

def test__BST_is_bst_satisified0():
    bst = BST()
    bst.root = Node(0)
    bst.root.left = Node(1)
    assert not bst.is_bst_satisfied()

def test__BST_is_bst_satisified1():
    bst = BST()
    bst.root = Node(0)
    bst.root.left = Node(-2)
    bst.root.left.left = Node(-3)
    bst.root.left.right = Node(-1)
    bst.root.right = Node(2)
    bst.root.right.left = Node(1)
    bst.root.right.right = Node(-3)
    assert not bst.is_bst_satisfied()

def test__BST_is_bst_satisfied2():
    bst = BST()
    bst.root = Node(-2)
    bst.root.left = Node(-3)
    bst.root.right = Node(-4)
    assert not bst.is_bst_satisfied()

def test__BST_is_bst_satisified3():
    bst = BST()
    assert bst.is_bst_satisfied()

def test__BST_is_bst_satisified4():
    bst = BST()
    bst.root = Node(0)
    bst.root.left = Node(-1)
    assert bst.is_bst_satisfied()

def test__BST_is_bst_satisified5():
    bst = BST()
    bst.root = Node(0)
    bst.root.left = Node(-2)
    bst.root.left.left = Node(-3)
    bst.root.left.right = Node(-1)
    bst.root.right = Node(2)
    bst.root.right.left = Node(1)
    bst.root.right.right = Node(3)
    assert bst.is_bst_satisfied()

def test__BST_is_bst_satisified6():
    bst = BST()
    bst.root = Node(0)
    bst.root.left = Node(-2)
    bst.root.left.left = Node(-3)
    bst.root.left.right = Node(-1)
    bst.root.right = Node(2)
    bst.root.right.left = Node(-1)
    bst.root.right.right = Node(3)
    assert not bst.is_bst_satisfied()

def test__BST_is_bst_satisified7():
    bst = BST()
    bst.root = Node(0)
    bst.root.left = Node(-2)
    bst.root.left.left = Node(-3)
    bst.root.left.right = Node(1)
    bst.root.right = Node(2)
    bst.root.right.left = Node(1)
    bst.root.right.right = Node(3)
    assert not bst.is_bst_satisfied()

################################################################################

import random
import copy
from hypothesis import given
import hypothesis.strategies as st
ints = st.lists(st.integers())


@given(xs=ints)
def test__BST_insert(xs):
    xs = list(set(xs))
    bst = BST()
    for x in xs:
        bst.insert(x)
        assert x in bst.to_list('inorder')
        assert bst.is_bst_satisfied()
    

@given(xs=ints)
def test__BST_insert_list(xs):
    xs = list(set(xs))
    bst = BST()
    bst.insert_list(xs)
    assert bst.is_bst_satisfied()
    

@given(xs=ints)
def test__BST___init__(xs):
    xs = list(set(xs))
    bst = BST(xs)
    assert bst.is_bst_satisfied()


@given(xs=ints)
def test__BST___contains__1(xs):
    '''
    Checks that if a value is in the bst then __contains__ returns True
    '''
    xs = list(set(xs))
    if len(xs)>0:
        x = random.choice(xs)
        bst = BST(xs)
        assert x in bst


@given(xs=ints)
def test__BST___contains__2(xs):
    '''
    Checks that if a value is NOT in the bst then __contains__ returns False
    '''
    xs = list(set(xs))
    if len(xs)>0:
        while True:
            x = random.uniform(min(xs)-1,max(xs)+1)
            if x not in xs:
                break
    else:
        x = 10
    bst = BST(xs)
    assert x not in bst


@given(xs=ints)
def test__BST_find_smallest(xs):
    xs = list(set(xs))
    if len(xs)>0:
        x = min(xs)
        bst = BST(xs)
        assert x == bst.find_smallest()


@given(xs=ints)
def test__BST_find_largest(xs):
    xs = list(set(xs))
    if len(xs)>0:
        x = max(xs)
        bst = BST(xs)
        assert x == bst.find_largest()


@given(xs=ints)
def test__BST_remove1(xs):
    '''
    This tests the remove function.
    In order to test the remove function, we must be able to generate valid BSTs.
    Therefore, you must have all the insert functionality completed before this test can pass.
    '''
    xs = list(set(xs))
    bst = BST(xs)
    while len(xs)>0:
        x = random.choice(xs)
        xs.remove(x)
        assert x in bst
        bst.remove(x)
        assert x not in bst
        assert bst.to_list('inorder')==sorted(xs)
        assert bst.is_bst_satisfied()


@given(xs=ints)
def test__BST_remove2(xs):
    '''
    If we remove something from the BST that is not in the BST,
    then the BST should remain unchanged.
    '''
    xs = list(set(xs))
    bst = BST(xs)
    y = 0
    while y in xs:
        y += 1
    bst.remove(y)
    assert bst.to_list('inorder')==sorted(xs)


@given(xs=ints, ys=ints)
def test__BST_remove_list1(xs,ys):
    xs = list(set(xs))
    bst = BST(xs)
    bst.remove_list(ys)
    for y in ys:
        assert y not in bst


@given(xs=ints, ys=ints)
def test__BST_remove_list2(xs,ys):
    xs = list(set(xs))
    bst = BST(xs)
    bst.remove_list(ys)
    for y in ys:
        if y in xs:
            xs.remove(y)
    assert bst.to_list('inorder') == sorted(xs)


@given(xs=ints,ys=ints)
def test__BST_remove_and_insert1(xs,ys):
    '''
    This test performs a mixture of both insertions and removals.
    This ensures that there are no weird interactions between inserting and removing.
    '''
    xs = list(set(xs))
    bst = BST(xs)
    for y in ys:
        bst.insert(y)
        x = random.choice(bst.to_list('inorder'))
        bst.remove(x)
        assert bst.is_bst_satisfied()


@given(xs=ints,ys=ints)
def test__BST_remove_and_insert2(xs,ys):
    '''
    This test performs a mixture of both insertions and removals.
    This ensures that there are no weird interactions between inserting and removing.
    '''
    xs = list(set(xs))
    bst = BST(xs)
    for y in ys:
        bst.insert(y)
        x = bst.find_largest()
        bst.remove(x)
        assert bst.is_bst_satisfied()


@given(xs=ints,ys=ints)
def test__BST_remove_and_insert3(xs,ys):
    '''
    This test performs a mixture of both insertions and removals.
    This ensures that there are no weird interactions between inserting and removing.
    '''
    xs = list(set(xs))
    bst = BST(xs)
    for y in ys:
        bst.insert(y)
        x = bst.find_smallest()
        bst.remove(x)
        assert bst.is_bst_satisfied()


@given(xs=ints)
def test__BST_inorder_property(xs):
    '''
    The order we insert objects into a BST can affect the structure of the tree,
    but it should NOT affect the list we get out from an inorder traversal.
    (Recall that the inorder traversal of a BST should always be a sorted list.)
    This test randomly shuffles the input list two different ways
    and checks that both shufflings give the same output list.
    This tests both the insertion functions and the traversal functions
    to ensure that there are no bad interactions between theses functions.
    '''
    xs = list(set(xs))

    xs1 = copy.copy(xs)
    random.shuffle(xs1)
    bst1 = BST(xs1)

    xs2 = copy.copy(xs)
    random.shuffle(xs2)
    bst2 = BST(xs2)
    
    assert bst1.to_list('inorder') == bst2.to_list('inorder')


def test__BST_iterable_1():
    '''
    The BST should be iterable.
    Iterating over the tree should give the results in sorted order.

    HINT:
    Currently, the BST class is not iterable because it does not define the __iter__ method.
    Therefore, these tests all fail.
    You must define an appropriate __iter__ method in order to make these tests pass.
    I encourage you to think carefully about how you can reuse your previously implemented functions to implement the iterable interface.
    '''
    xs = [1, 2, 3, 4, 5]
    bst = BST(xs)
    _iter = iter(bst)
    assert next(_iter) == 1
    assert next(_iter) == 2
    assert next(_iter) == 3
    assert next(_iter) == 4
    assert next(_iter) == 5
    try:
        next(_iter)
    except StopIteration:
        pass


@given(xs=ints)
def test__BST_iterable_2(xs):
    xs = list(set(xs))

    xs1 = copy.copy(xs)
    random.shuffle(xs1)
    bst1 = BST(xs1)

    xs2 = copy.copy(xs)
    random.shuffle(xs2)
    bst2 = BST(xs2)

    assert list(bst1) == list(bst2)


@given(xs=ints)
def test__BST_eq(xs):
    '''
    This test is essentially the same as the previous one,
    but tests the == operator specifically.
    '''
    xs = list(set(xs))

    xs1 = copy.copy(xs)
    random.shuffle(xs1)
    bst1 = BST(xs1)

    xs2 = copy.copy(xs)
    random.shuffle(xs2)
    bst2 = BST(xs2)
    
    assert bst1 == bst2
