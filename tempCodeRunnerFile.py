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
        '''finds'''
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
            return self._find(data, cur_node.right)
        if data == cur_node.data:
            return True
        return False