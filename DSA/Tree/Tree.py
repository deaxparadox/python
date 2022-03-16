#!/usr/bin/env python
# coding: utf-8

# **tree**
# 
# 1. abstract data type
# 2. each element has a parent execpt top element
# 3. zero or more children
# 4. top element is typically called root element
# 5. used for searching and data organization
# 
# 
# **Formal Tree Definitions**
# 
# 1. we define a *tree T* as a set of nodes string elements such that the nodes have a parent-child relationship that satisfies the following properties:
# 
# - If T is nonempty, it has a special node, called the *root* of *T*, that has a parent.
# - Each node *v* of *T* differnt from the root has a unique parent node *w*; every node with parent *w* is a *child* from *w*.
#         
# **Other Node Relationships**
# 
# - Two nodes that are children of the same parent are siblings
# - A node *v* is ***external*** if *v* has no children
# - A ndoe *v* is ***interval*** if it has one or more children. 
# - External nodes are also known as ***leaves***.
# 
# **Edges and Paths in Trees**
# 
# - An ***edge*** of tree *T* is a pair of nodes *(u,v)* such that u is that parent of *v*, or vice-versa.
# - A ***path*** of *T* is a sequence of nodes such that any two consecutive nodes the sequence from an edge.
# 
# **Ordered Trees**
# 
# - A tree is **ordered** if there is a meaningfull linear order among the children of each node; that is, we purposefull identify the children of a node as being the first, second, third, and so on. 

# # General form 

# In[25]:


"""Create a Node class that will represent a single node."""
class Node:
    def __init__(self, data) -> None:
        self.left = None 
        self.right = None 
        self.data = data 
    
    """Insert Method
    - insert compares the value of the node to the parent node and decides 
        to add it as a left node or a right node.
    - printTree() prints the tree.
    """
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data 
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
        

        
"""initializing a tree"""
root = Node(30)
# root.left = Node(34)
# root.left.left = Node(20)
# root.left.right = Node(45)
# root.right = Node(89)
# root.right.left = Node(56)
# root.right.right = Node(54)
"""after insert method in Node class"""
root.insert(15)
root.insert(40)
root.insert(35)
root.insert(12)
root.insert(20)
# root.PrintTree()

"""Every Node in a tree is visited three times.
    - There are three types of traversals in a binary tree
        1. in-order
        2. pre-order
        3. post-order
"""

"""In-order Traversal
    - visited the left child and perform recursion,
    - then we visit the same node for the second time to print the node
    - further followed by the parent node, then followed by recursion on the right child.
"""
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)
# print(inorder(root))

"""Post-order Traversal
    - while traversing a tree, we do recursion on the left node and the right node.
    - then we come to the root node to print it.
"""
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)
# print(postorder(root))


# # General Trees

# In[11]:


class Tree:
    """Abstract base class expresenting a tree structure."""
    
    #-----------------nested Position class------------------
    
    class Position:
        """An abstraction representing the location of a single element."""
        
        def element(self):
            """Return the element stored at this position."""
            raise NotADirectoryError("must be implemented by subclass")
        
        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError("must be implemented by subclass")
            
        def __ne__(self, other):
            """Return True if other does not repersent the same location."""
            return not (self==other)               # opposite of __eq__
        
    # abstract methods that concerte subclass must support 
    def root(self):
        """Return Position representnig the tree's root (or None if empty)."""
        raise NotImplementedError("must be implemented by subclass ")
        
    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)"""
        raise NotImplementedError("must be implemented by subclass")
        
    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError("must be implemented by subclass")
        
    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError("must be implemented by subclass")

    def __len__(self):
        """Raise the total number of elements in the tree."""
        raise NotImplementedError("must be implemented by subclass")
    
    # concreate methods implemented in this class 
    def is_root(self, p):
        """Return True if Positions p representeds the root of the tree."""
        return self.root() == p
    
    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0
    
    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0
    
    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1+self.depth(self.parent(p))
        
    def _height(self):
        """Return the height of the tree."""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))
    
    def _height2(self, p):
        """Return the height of the subtree rooted at Position p."""
        if self.is_leap(p):
            return 0
        else:
            return 1+max(self._height2(c) for c in self.children(p))
        
    def height(self, p=None):
        """Return the height of the subtree rooted at position p.
        
        If p is None, return the height of the entire tree."""
        
        if p is None:
            p = self.root()
        return self._height2(p)      # start _height2 recursion


# # Binary Trees

# In[27]:


class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""
    
    # ---------- additinoal abstract methods -------------
    def left(self, p):
        """Return a Position representing p's left child.
        
        Return None if p does not have a left child."""
        raise NotImplementedError("must be implemented by subclass")
        
    def right(self,p):
        """Return a Position representing p's right child.
        
        Return None if p does not have a right child."""
        raise NotImplementedError("must be implemented by subclass")
        
    # -------- concrete methods implemented in this class ---------
    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:              # p must be the root 
            return None                 # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)          # possibly None 
            else:
                return self.left(parent)           # possibly None
    
    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


# # Implementing Trees

# In[33]:


class LinkedBiaryTree(BinaryTree):
    """Linked repersentation of a binary tree structure."""
    
    class _Node:      # Lightweight, nonpublic class for string a node 
        __slots__ = "_element", "_parent", "_left", "_right"
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent 
            self._left = left 
            self._right = right 
            
    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element."""
        
        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container 
            self._node = node 
        
        def element(self):
            """Return the element stored at this Position."""
            return self._node._element
        
        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node
        
        def _validate(self, p):
            """Return associated node, if position is valid."""
            if not isinstance(p, self.Position):
                raise TypeError("p must be proper Position type")
            if p._container is not self:
                raise ValueError("p does not belong to this container")
            if p._node._parent is p._node:     # convention for deprecated node 
                raise ValueError('p is no longer valid')
            return p._node 
        
        def _make_position(self, node):
            """Return Position for given ndoe (or None if no node.)"""
            return self.Position(self, node) if node is not None else None
                
            
    # --------- binary tree constructore ----------
    def __init__(self):
        """Create an initally empty binary tree."""
        self._root = Noen 
        self._size = 0
    
    # -------- public accessors ------------------
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size 
    
    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)
    
    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)
    
    def left(self, p):
        """Return the Position of p's left child (or None if no left child)."""
        node = self._validate(p)
        return self._make_position(node._left)
    
    def right(self, p):
        """Return the Position of p's right child (or None if no right child)."""
        node = self._validate(p)
        return self._make_position(node._right)
    
    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:        # left child exists
            count += 1
        if node._right is not None:        # right child exists 
            count += 1
        return count 
    
    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.
        
        Raise ValueError it tree nonempty.
        """
        
        if self._root is not None: raise ValueError("Root exists")
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)
    
    def _add_left(self, p, e):
        """Create a new left child for Position p, storing element e.
        
        Return the Position of new ndoe.
        Raise ValueError if Position p is invalid or p already has a left child.
        """
        node = self._validate(p)
        if node._left is not None: raise ValueError('Left child exists.')
        self._size += 1
        node._left = self._Node(e, node)               # node is its parent 
        return self._make_position(node._left)
    
    
    def _add_right():
        """Create a new right child for Position p, storing element e.
        
        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        node = self._validate(p)
        if node._right is not None: raise ValueError("Right child exists")
        self._size += 1
        node._right = self._Node(e, node)            # node is its parent 
        return self._make_position(node._right)
    
    def _replace(self, p, e):
        """Replace the element at position p with e, and return old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old 
    
    
    def _delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any 
        
        Return the element hat had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two cildren.
        """
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError("p has two children")
        child = node._left if node._left else node._right     # might be None 
        if child is not None:
            child._parent = node._parent     # child's grandparent becomes parent
        if node is self._root:
            self._root = child               # child becomes root 
        else:
            parent = node._parent 
            if node is parent._left:
                parent._left = child 
            else:
                parent._right = child 
        self._size -= 1
        node._parent = node                  # convention for deprecated node 
        return node._element

    def _attack(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p."""
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError("position must be leaf")
        if not type(self) is type(t1) is type(t2):    # all 3 trees must be same type 
            raise TypeError("Tree types must match")
        self._size += len(t1) + len(t2)
        if not t1.is_empty():               # attached t1 as left subtree of node 
            t1._root._parent = node 
            node._left = t1._root 
            t1._root = None                 # set t1 instance to empty
            t1._size = 0
        if not t2.is_empty():               # attach t2 as right subtree of node 
            t2._root._parent = node 
            node._right = t2._root 
            t2._root = None                 # set t2 instance to empty 
            t2._size = 0
            


# **Array-Based Representation of a Binary Tree**

# In[ ]:




