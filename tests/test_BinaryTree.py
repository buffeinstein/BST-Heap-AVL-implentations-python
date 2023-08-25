from containers.BinaryTree import BinaryTree, Node


_example0 = BinaryTree()

_example1 = BinaryTree()
_example1.root = Node(1)
_example1.root.left = Node(2)
_example1.root.left.left = Node(4)
_example1.root.left.right = Node(5)
_example1.root.right = Node(3)

_example2 = BinaryTree()
_example2.root = Node(0)
_example2.root.left = Node(1)
_example2.root.left.left = Node(2)
_example2.root.left.left.left = Node(3)
_example2.root.left.left.left.left = Node(4)
_example2.root.left.left.left.left.left = Node(5)
_example2.root.left.left.left.left.left.left = Node(6)
_example2.root.left.left.left.left.left.right = Node(7)
_example2.root.left.left.right = Node(8)
_example2.root.left.left.right.left = Node(9)
_example2.root.left.left.right.right = Node(10)
_example2.root.left.right = Node(11)
_example2.root.right = Node(12)
_example2.root.right.right = Node(13)
_example2.root.right.right.right = Node(14)

_example3 = BinaryTree()
_example3.root = Node(0)
_example3.root.left = Node(1)
_example3.root.left.left = _example1.root
_example3.root.left.left = _example2.root
_example3.root.right = _example2.root


def test__BinaryTree_preorder_print0():
    assert _example0.print_tree('preorder') == ''

def test__BinaryTree_preorder_print1():
    assert _example1.print_tree('preorder') == '1-2-4-5-3-'

def test__BinaryTree_preorder_print2():
    assert _example2.print_tree('preorder') == '0-1-2-3-4-5-6-7-8-9-10-11-12-13-14-'

def test__BinaryTree_preorder_print3():
    assert _example3.print_tree('preorder') == '0-1-0-1-2-3-4-5-6-7-8-9-10-11-12-13-14-0-1-2-3-4-5-6-7-8-9-10-11-12-13-14-'


def test__BinaryTree_inorder_print0():
    assert _example0.print_tree('inorder') == ''

def test__BinaryTree_inorder_print1():
    assert _example1.print_tree('inorder') == '4-2-5-1-3-'

def test__BinaryTree_inorder_print2():
    assert _example2.print_tree('inorder') == '6-5-7-4-3-2-9-8-10-1-11-0-12-13-14-'

def test__BinaryTree_inorder_print3():
    assert _example3.print_tree('inorder') == '6-5-7-4-3-2-9-8-10-1-11-0-12-13-14-1-0-6-5-7-4-3-2-9-8-10-1-11-0-12-13-14-'


def test__BinaryTree_postorder_print0():
    assert _example0.print_tree('postorder') == ''

def test__BinaryTree_postorder_print1():
    assert _example1.print_tree('postorder') == '4-5-2-3-1-'

def test__BinaryTree_postorder_print2():
    assert _example2.print_tree('postorder') == '6-7-5-4-3-9-10-8-2-11-1-14-13-12-0-'

def test__BinaryTree_postorder_print3():
    assert _example3.print_tree('postorder') == '6-7-5-4-3-9-10-8-2-11-1-14-13-12-0-1-6-7-5-4-3-9-10-8-2-11-1-14-13-12-0-0-'


def test__BinaryTree_preorder0():
    assert _example0.to_list('preorder') == []

def test__BinaryTree_preorder1():
    assert _example1.to_list('preorder') == [1, 2, 4, 5, 3, ]

def test__BinaryTree_preorder2():
    assert _example2.to_list('preorder') == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, ]

def test__BinaryTree_preorder3():
    assert _example3.to_list('preorder') == [0, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, ]


def test__BinaryTree_inorder0():
    assert _example0.to_list('inorder') == []

def test__BinaryTree_inorder1():
    assert _example1.to_list('inorder') == [4, 2, 5, 1, 3]

def test__BinaryTree_inorder2():
    assert _example2.to_list('inorder') == [6, 5, 7, 4, 3, 2, 9, 8, 10, 1, 11, 0, 12, 13, 14]

def test__BinaryTree_inorder3():
    assert _example3.to_list('inorder') == [6, 5, 7, 4, 3, 2, 9, 8, 10, 1, 11, 0, 12, 13, 14, 1, 0, 6, 5, 7, 4, 3, 2, 9, 8, 10, 1, 11, 0, 12, 13, 14]


def test__BinaryTree_postorder0():
    assert _example0.to_list('postorder') == []

def test__BinaryTree_postorder1():
    assert _example1.to_list('postorder') == [4, 5, 2, 3, 1]

def test__BinaryTree_postorder2():
    assert _example2.to_list('postorder') == [6, 7, 5, 4, 3, 9, 10, 8, 2, 11, 1, 14, 13, 12, 0]

def test__BinaryTree_postorder3():
    assert _example3.to_list('postorder') == [6, 7, 5, 4, 3, 9, 10, 8, 2, 11, 1, 14, 13, 12, 0, 1, 6, 7, 5, 4, 3, 9, 10, 8, 2, 11, 1, 14, 13, 12, 0, 0]


def test__BinaryTree_height0():
    assert _example0.height() == -1

def test__BinaryTree_height1():
    assert _example1.height() == 2

def test__BinaryTree_height2():
    assert _example2.height() == 6

def test__BinaryTree_height3():
    assert _example3.height() == 8


def test__BinaryTree_size0():
    assert _example0.__len__() == 0

def test__BinaryTree_size1():
    assert _example1.__len__() == 5

def test__BinaryTree_size2():
    assert _example2.__len__() == 15

def test__BinaryTree_size3():
    assert _example3.__len__() == 32


def test__BinaryTree_len0():
    assert len(_example0) == 0

def test__BinaryTree_len1():
    assert len(_example1) == 5

def test__BinaryTree_len2():
    assert len(_example2) == 15

def test__BinaryTree_len3():
    assert len(_example3) == 32
