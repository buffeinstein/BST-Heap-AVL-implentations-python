from containers.BinaryTree import BinaryTree, Node
from containers.Heap import Heap


def test__Heap_super():
    x = Heap()
    assert isinstance(x,BinaryTree)


# the very first thing to do whenever creating a data structure 
# is to write a function to check if the invariant holds 
# (in this case the Heap property)
# and create test cases for whether that function works

def test__Heap_is_heap_satisified1():
    heap = Heap()
    heap.root = Node(0)
    heap.root.left = Node(2)
    heap.root.left.left = Node(2)
    heap.root.left.right = Node(5)
    heap.root.right = Node(0)
    heap.root.right.left = Node(0)
    heap.root.right.right = Node(30)
    assert heap.is_heap_satisfied()

def test__Heap_is_heap_satisfied2():
    heap = Heap()
    heap.root = Node(-2)
    heap.root.left = Node(3)
    heap.root.right = Node(4)
    assert heap.is_heap_satisfied()

def test__Heap_is_heap_satisified3():
    heap = Heap()
    assert heap.is_heap_satisfied()

def test__Heap_is_heap_satisified4():
    heap = Heap()
    heap.root = Node(0)
    heap.root.left = Node(-1)
    assert not heap.is_heap_satisfied()

def test__Heap_is_heap_satisified5():
    heap = Heap()
    heap.root = Node(0)
    heap.root.left = Node(-2)
    heap.root.left.left = Node(-3)
    heap.root.left.right = Node(-1)
    heap.root.right = Node(2)
    heap.root.right.left = Node(1)
    heap.root.right.right = Node(3)
    assert not heap.is_heap_satisfied()

def test__Heap_is_heap_satisified6():
    heap = Heap()
    heap.root = Node(0)
    heap.root.left = Node(2)
    heap.root.left.left = Node(3)
    heap.root.left.right = Node(5)
    heap.root.right = Node(1)
    heap.root.right.left = Node(4)
    heap.root.right.right = Node(-1)
    assert not heap.is_heap_satisfied()

################################################################################

import random
import copy
from hypothesis import given
import hypothesis.strategies as st
ints = st.lists(st.integers())


@given(xs=ints)
def test__Heap_insert(xs):
    xs = list(xs)
    heap = Heap()
    for x in xs:
        heap.insert(x)
        assert x in heap.to_list('inorder')
        assert heap.is_heap_satisfied()
    

@given(xs=ints)
def test__Heap_insert_list(xs):
    xs = list(xs)
    heap = Heap()
    heap.insert_list(xs)
    assert heap.is_heap_satisfied()
    for x in xs:
        assert x in heap.to_list('inorder')
    

@given(xs=ints)
def test__Heap___init__(xs):
    xs = list(xs)
    heap = Heap(xs)
    assert heap.is_heap_satisfied()
    for x in xs:
        assert x in heap.to_list('inorder')


@given(xs=ints)
def test__Heap_find_smallest1(xs):
    xs = list(xs)
    if len(xs)>0:
        x = min(xs)
        heap = Heap(xs)
        assert x == heap.find_smallest()


@given(xs=ints)
def test__Heap_find_smallest2(xs):
    xs = list(xs)
    if len(xs)>0:
        x = min(xs)
        heap = Heap(xs)
        assert x == heap.find_smallest()


@given(xs=ints)
def test__Heap_remove1(xs):
    '''
    This tests the remove function.
    In order to test the remove function, we must be able to generate valid Heaps.
    Therefore, you must have all the insert functionality completed before this test can pass.
    '''
    xs = list(xs)
    heap = Heap(xs)
    while len(xs)>0:
        x = min(xs)
        xs.remove(min(xs))
        assert x in heap.to_list('inorder')
        heap.remove_min()
        assert heap.is_heap_satisfied()


@given(xs=ints)
def test__Heap_remove2(xs):
    '''
    This tests the remove function.
    In order to test the remove function, we must be able to generate valid Heaps.
    Therefore, you must have all the insert functionality completed before this test can pass.
    '''
    xs = list(set(xs))
    heap = Heap(xs)
    while len(xs)>0:
        x = min(xs)
        xs.remove(min(xs))
        assert x in heap.to_list('inorder')
        heap.remove_min()
        assert x not in heap.to_list('inorder')
        assert heap.is_heap_satisfied()


@given(xs=ints,ys=ints)
def test__Heap_remove_and_insert1(xs,ys):
    '''
    This test performs a mixture of both insertions and removals.
    This ensures that there are no weird interactions between inserting and removing.
    '''
    xs = list(xs)
    heap = Heap(xs)
    for y in ys:
        heap.insert(y)
        heap.remove_min()
        assert heap.is_heap_satisfied()


@given(xs=ints,ys=ints)
def test__Heap_remove_and_insert2(xs,ys):
    '''
    This test performs a mixture of both insertions and removals.
    This ensures that there are no weird interactions between inserting and removing.
    '''
    xs = list(xs)
    heap = Heap(xs)
    for y in ys:
        heap.insert(y)
        heap.remove_min()
        assert heap.is_heap_satisfied()
