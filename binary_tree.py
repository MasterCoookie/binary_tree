r'''Binary trees are somewhat related to linked lists. They also consist of
Node() objects. Instead of head, there is a root node which reprents the first node. Each
node points to two more, making a tree of nodes that looks something like this:
       1
    /     \
   2       3
 /   \   /   \
4     5 6     7
Where 1 is a root node and 4, 5, 6 and 7 are called leaves nodes.
The tree in this ex has depth of 3 and is a full (proper/plane) tree
(each node has either 2 or 0 children).

Binary search trees adiffer from binary trees in that the entries are ordered.
The left node is allaways less then ints previous and right is alaways grater. ex:
       8
    /     \
   3       10
 /   \   /   \
1     6      14
'''
class Node():
    '''A single part of binary tree'''
    def __init__(self, data):
        '''unlike in linked lists, there is no .next pointer. There are
        .left and .right properties (pointers) instead. Initially both set to none.'''
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    '''A whole tree consists of separate Node() objects'''
    def __init__(self, root):
        '''Assigning the root node'''
        self.root = Node(root)

    def print_tree(self, traversal_type):
        '''prints the tree in a specified way.

        traversal_type -> For now only supports the pre-order way
        Input "preorder" for pre-order print'''     
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")
        
        print("Traversal type", str(traversal_type), "is not supported")
        return False

    def preorder_print(self, start, traversal):
        '''Going through a tree in pre-order way is basically
        going from the root to the left, if there is no left checking right. If there
        is no right either going up one node.

        start -> updated each time as the method works recursive
        traversal -> final string of values to be printed, separated by -
        For the ex in the file docstring the resoult will be 1-2-4-5-3-6-7-'''
        if start:
            traversal += (str(start.data) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        '''Going through tree in pre-order way: go left as far as possible, then root, then right.

        start -> updated each time as the method works recursive
        traversal -> final string of values to be printed, separated by -

        For the ex in the file docstring the resoult will be:
        4-2-5-1-6-3-7'''
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.data) + '-')
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        '''Going through tree in post-order way: go left as far as possible, then right, then root.

        start -> updated each time as the method works recursive
        traversal -> final string of values to be printed, separated by -

        For the ex in the file docstring the resoult will be:
        4-2-5-6-3-7-1'''
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.data) + '-')
        return traversal

class BinarySearchTree():
    '''A binary search tree is a binary tree which Nodes are sorted.
    More suitable to work on.'''
    def __init__(self):
        self.root = None

    def insert(self, data):
        '''Inserts a new node, uses ._insert() recursive helper method to
        sort the data while inserting
        data -> data of the new node'''
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
    
    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                # if left node already exists, move to the left
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                # if right node already exists, move to the right
                self._insert(data, cur_node.right)
        else:
            print("Value already present in tree, no duplicates allowed.")

    def find(self, data):
        '''Finds given data in a tree.
        Uses helper method _find that works recursive.
        data -> data to look for
        Returns True if data is present in a tree, False if it isn't or None if no tree is empty'''
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data == cur_node.data:
            return True
        return False

def main():
    '''main, just for testing'''
    # tree = BinaryTree(1)
    # tree.root.left = Node(2)
    # tree.root.right = Node(3)
    # tree.root.left.left = Node(4)
    # tree.root.left.right = Node(5)
    # tree.root.right.left = Node(6)
    # tree.root.right.right = Node(7)
    # #tree.root.right.right.right = Node(8)

    # print(tree.print_tree("preorder"))
    # print(tree.print_tree("inorder"))
    # print(tree.print_tree("postorder"))
    BST = BinarySearchTree()
    BST.insert(4)
    BST.insert(2)
    BST.insert(8)
    BST.insert(5)
    BST.insert(10)
    print(BST.find(4))

if __name__ == "__main__":
    main()
