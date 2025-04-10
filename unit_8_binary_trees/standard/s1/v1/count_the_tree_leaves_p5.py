"""
    Prompt:

    You've grown an oak tree from a tiny little acorn and it's finally sprouting leaves! 

    Given the 'root' of a binary tree representing your oak tree, count the number of leaf
    nodes in the tree. A leaf node is a node that does not have any children

    Evaluate the time complexity of your solution. Define your variables and provide a 
    rationale for why you believe your solution has the stated time complexity. Assume
    the input tree is balanced when calculating time complexity.
"""

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_leaves(root: TreeNode):
    if not root:
        return 0
    
    def recursion(node: TreeNode):
        if not node.left and not node.right:
            return 1
        
        left_count = recursion(node.left) if node.left else 0
        right_count = recursion(node.right) if node.right else 0

        return left_count + right_count
    
    return recursion(root) 

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

oak1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


print(count_leaves(oak1)) # 3
print(count_leaves(oak2)) # 1