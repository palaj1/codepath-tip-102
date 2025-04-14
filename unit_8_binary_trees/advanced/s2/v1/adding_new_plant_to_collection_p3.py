"""
    Prompt:

    You have just purhcased a new housplant and are excited to add it to your collection! 
    
    Your collection is meticulously organized using a Binary Search Tree (BST) where each 
    node in the tree represents a houseplant in your collection, and houseplants are 
    organized alphabetically by name ('val')

    Given that root of your BST 'collection' and a new houseplant 'name', insert a new node 
    with value 'name' into your collection. Return the root of your updated collection. If 
    another plant with 'name' already exists in the tree, add the new node in the existing 
    node's right subtree.

    Evaluate the time and space complexity of your function. Define your variables and 
    provide a rationale for why you believe your solution has the stated time and space 
    complexity. Assume the input tree is balanced when calculating time and space complexity.
"""

from helpers.tree import build_tree, print_tree

from helpers.tree import TreeNode

def add_plant(collection: TreeNode, name: str) -> TreeNode:
    if not collection:
        return TreeNode(name)
    
    def bst_insertion(node: TreeNode):

        # duplicate found, insert to the right of subtree
        if name == node.val:
            if node.right:
                bst_insertion(node.right)
            else:
                node.right = TreeNode(name)
        elif name < node.val:
            if node.left:
                bst_insertion(node.left)
            else:
                node.left = TreeNode(name)
        else:
            if node.right:
                bst_insertion(node.right)
            else:
                node.right = TreeNode(name)
    
    bst_insertion(collection)
    
    return collection


values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)

# ================= Test New Node Insertion =================
# Expected Output = ['Money Tree', 'Fiddle Leaf Fig', 'Snake Plant', 'Aloe']
print(print_tree(add_plant(collection, "Aloe")))

# ================= Test Duplicate Insertion =================
add_plant(collection, "Aloe")

# Expected Output will contain None values due to level-order traversal
print(print_tree(collection))
# Expected Output = ['Money Tree', 'Fiddle Leaf Fig', 'Snake Plant', 'Aloe', None, None, None, None, 'Aloe']  
# Expected right child of 'Snake Plant's left child 'Aloe' = 'Aloe'
