"""
    Prompt:

    You are looking to buy a new flower plant for your garden. The nursery you visit stores 
    its inventory in a binary search tree (BST) where each node represents a plant in the 
    store. The plants are organized according to their names ('val's) in alphabetical order 
    in the BST.

    Given the root of the binary search tree 'inventory' and a target flower 'name', write
    a function find_flower() that returns 'True' if the flower is present in the garden and
    'False' otherwise.

    Evaluate the time and space complexity of your function. Define your variables and 
    provide a rationale for why you believe your solution has the stated time and space 
    complexity. Assume the input tree is balanced when calculating time and space complexity.
"""

from helpers.tree import build_tree, TreeNode

def find_flower(inventory: TreeNode, name: str):
    if not inventory:
        return False
    
    def binary_search(node: TreeNode):
        if not node:
            return False

        if node.val == name:
            return True

        if name < node.val:
            return binary_search(node.left)        
        else:
            return binary_search(node.right)        

    return binary_search(inventory)


# using build_tree() function at top of page
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))  # True
print(find_flower(garden, "Sunflower"))  # False