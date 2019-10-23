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
(each node has either 2 or 0 children).'''
class Node():
    '''A single part of binary tree'''
    def __init__(self, data):
        '''unlike in linked lists, there is no .next pointer. There are
        .left and .right properties (pointers) instead. Initially both set to none.'''
        self.data = data
        self.left = None
        self.right = None

class Queue():
    '''A modified list, created to store node objects'''
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        '''Adds a new node to a queue'''
        self.items.insert(0, item)


    def dequeue(self):
        '''Removes last node in a Queue()'''
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        '''Returns True if Queue() is empty.'''
        return len(self.items) == 0
    
    def peek(self):
        '''Returns a value of last node in a Queue()'''
        if not self.is_empty():
            return self.items[-1].data
        return None

    def __len__(self):
        return self.size()

    def size(self):
        '''Returns the number of items in a Queue()'''
        return len(self.items)

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
        elif traversal_type == "levelorder":
            return self.levelorder_print(self.root)
        
        print("Traversal type", str(traversal_type), "is not supported")
        return False

    def preorder_print(self, start, traversal):
        '''Going through a tree in pre-order way is basically
        going from the root to the left, if there is no left checking right. If there
        is no right either going up one node.

        start -> updated each time as the method works recursive
        traversal -> final string of values to be printed, separated by -
        For the ex in the file docstring the result will be 1-2-4-5-3-6-7-'''
        if start:
            traversal += (str(start.data) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        '''Going through tree in pre-order way: go left as far as possible, then root, then right.

        start -> updated each time as the method works recursive
        traversal -> final string of values to be printed, separated by -

        For the ex in the file docstring the result will be:
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

        For the ex in the file docstring the result will be:
        4-2-5-6-3-7-1'''
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.data) + '-')
        return traversal

    def levelorder_print(self, start):
        '''Going through tree in level-order way: go from top to bottom, left to right
        as you were reading a normal text.

        start -> starting node
        For the ex in the file docstring the result will be 1-2-3-4-5-6-7'''

        if start is None:
            return None

        queue = Queue()
        queue.enqueue(start)

        traversal = ""

        while len(queue):
            traversal += str(queue.peek()) + '-'
            node_removed = queue.dequeue()

            if node_removed.left:
                queue.enqueue(node_removed.left)

            if node_removed.right:
                queue.enqueue(node_removed.right)

        return traversal

    def height(self, node):
        '''Returns the height of a tree.
        Works recursively.
        Is extirmely hard to explain how it works, but this video explains it quite well:
        https://www.youtube.com/watch?v=BDw8zzy3QiY.
        For the tree in file docstring it would return 2.'''
        # if we hit empty node return -1 that will become 0 when returning
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)


def main():
    '''main, just for testing'''
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    # tree.root.right.left = Node(6)
    # tree.root.right.right = Node(7)
    #tree.root.right.right.right = Node(8)

    # print(tree.print_tree("preorder"))
    # print(tree.print_tree("inorder"))
    # print(tree.print_tree("postorder"))
    # print(tree.print_tree("levelorder"))
    print(tree.height(tree.root))

if __name__ == "__main__":
    main()
