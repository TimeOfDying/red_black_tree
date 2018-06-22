import unittest
from rbtree import RBtree, Node

class RbTreeTests(unittest.TestCase):
    
    def test_find_node(self):
        rb_tree = RBtree()
        rb_tree.insert(2)
        node_2 = rb_tree.root
        rb_tree.insert(1)
        node_1 = rb_tree.root.left
        rb_tree.insert(4)
        node_4 = rb_tree.root.right
        rb_tree.insert(5)
        node_5 = node_4.right
        rb_tree.insert(9)
        node_9 = node_5.right
        rb_tree.insert(3)
        node_3 = node_4.left
        rb_tree.insert(6)
        node_6 = node_9.left
        rb_tree.insert(7)
        node_7 = node_5.right
        rb_tree.insert(15)
        node_15 = node_9.right

        self.assertEqual(rb_tree.search(5), node_5)
        self.assertEqual(rb_tree.search(2), node_2)
        self.assertEqual(rb_tree.search(1), node_1)
        self.assertEqual(rb_tree.search(4), node_4)
        self.assertEqual(rb_tree.search(3), node_3)
        self.assertEqual(rb_tree.search(7), node_7)
        self.assertEqual(rb_tree.search(6), node_6)
        self.assertEqual(rb_tree.search(9), node_9)
        self.assertEqual(rb_tree.search(15), node_15)
    
    def test_Insert(self):
        tree = RBtree()
        tree.insert(20)
        tree.insert(15)
        tree.insert(25)
        tree.insert(10)
        
        self.assertEqual(tree.root.red, False)
        self.assertEqual(tree.search(15).red, False)
        self.assertEqual(tree.search(25).red, False)
        tree.insert(17)
        tree.insert(8)
        self.assertEqual(tree.search(15).red, True)
        self.assertEqual(tree.search(10).red, False)
        self.assertEqual(tree.search(17).red, False)
        self.assertEqual(tree.search(8).red, True)
        tree.insert(9) 
        self.assertEqual(tree.search(10).red, True)
        self.assertEqual(tree.search(8).red, True)
        self.assertEqual(tree.search(9).left.key, 8)
        
    def test_Delete(self):
        tree = RBtree()
        tree.insert(20)
        tree.insert(15)
        tree.insert(25)
        tree.insert(23)
        tree.insert(27)
        self.assertEqual(tree.root.red, False);
        self.assertEqual(tree.root.right.key, 25);
        self.assertEqual(tree.root.right.left.key, 23);
        self.assertEquals(tree.root.right.left.red, True);
        tree.deleteNode(25);
        self.assertEqual(tree.root.key, 20);
        self.assertEqual(tree.root.right.key, 27);
        self.assertEqual(tree.root.right.red, False);
        self.assertEqual(tree.root.right.right.key, None);
        self.assertEqual(tree.root.right.left.key, 23);
        self.assertEqual(tree.root.right.left.red, True); 
        
    def test_root_delete(self):
        rb_tree = RBtree()
        root = Node(5)
        root.red = False
        left_child = Node(3)
        left_child.red = True
        left_child.parent = root
        left_child.left = Node(None)
        left_child.right = Node(None)
        right_child = Node(8)
        right_child.red = True
        right_child.parent = root
        right_child.left = Node(None)
        right_child.right = Node(None)
        root.left = left_child
        root.right = right_child  
        rb_tree.root = root
        rb_tree.deleteNode(5)

        self.assertEqual(rb_tree.root.key, 8)
        self.assertEqual(rb_tree.root.left.key, 3)
        
unittest.main() 