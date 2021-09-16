"""
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Design an algorithm to insert a new node to a complete binary tree keeping it complete after the insertion.

Implement the CBTInserter class:

CBTInserter(TreeNode root) Initializes the data structure with the root of the complete binary tree.

int insert(int v) Inserts a TreeNode into the tree with value Node.val == val so that the tree remains complete, and returns the value of the parent of the inserted TreeNode.
TreeNode get_root() Returns the root node of the tree.

"""

class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 


class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.insert_order = []
        self.bfs_tree()
        print(self.insert_order)

    def bfs_tree(self):
        queue=[self.root]
        while queue:
            node = queue.pop(0)
            if(not node.left or not node.right):
                self.insert_order.append(node)
            if(node.left):
                queue.append(node.left)
            if(node.right):
                queue.append(node.right)

        
    def insert(self, val: int) -> int:
        self.insert_order = []
        self.bfs_tree()
        nd = TreeNode(val)
        insert_node = self.insert_order[0]
        if(not insert_node.left):
            insert_node.left = nd
        elif(not insert_node.right):
            insert_node.right = nd
            self.insert_order.pop(0)
        return insert_node.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root


