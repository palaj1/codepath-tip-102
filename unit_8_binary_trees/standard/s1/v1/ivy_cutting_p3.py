"""
  Prompt:

  You have a trailing ivy plant represented by a binary tree. You want to take a cutting to
  start a new plant using the rightmost vine in the plant. Given the 'root' of the plant, 
  return a list with the value of each node in the path from the 'root' node to the 
  rightmost leaf node.

  Evaluate the time complexity of your function. Define your variables and provide a 
  rationale for why you believe your solution has the stated time complexity. Assume the 
  input tree is balanced when calculating time complexity.
"""

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root: TreeNode):
    if not root:
        return []
    
    return [root.val] + right_vine(root.right)

"""
 if not root:
        return []
    return [root.val] + right_vine_recursive(root.right)
    print("Right Vine (Recursive):", right_vine_recursive(root))
"""


"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))