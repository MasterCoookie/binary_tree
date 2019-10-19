r'''Binary search trees adiffer from binary trees in that the entries are ordered.
The left node is allaways less then ints previous and right is alaways grater. ex:
       8
    /     \
   3       10
 /   \   /   \
1     6      14'''

class Node():
    '''A single part of binary tree'''
    def __init__(self, data):
        '''unlike in linked lists, there is no .next pointer. There are
        .left and .right properties (pointers) instead. Initially both set to none.'''
        self.data = data
        self.left = None
        self.right = None

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
    BST = BinarySearchTree()
    BST.insert(8)
    BST.insert(3)
    BST.insert(10)
    BST.insert(1)
    BST.insert(6)
    BST.insert(9)
    BST.insert(11)
    # print(BST.find(4))

if __name__ == "__main__":
    main()
