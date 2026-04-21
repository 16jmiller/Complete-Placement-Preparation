# Count the number of subtrees within a tree where all of the nodes in a subtree have the same value

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.has_identical_subtree = False
        self.left:BinaryTreeNode = None
        self.right:BinaryTreeNode = None

def count_subtrees_with_same_values(bt_primary_node:BinaryTreeNode):
    # mark subtrees as valid via a postorder traversal
    identical_value_subtree_count = 0
    
    # build node list
    bfs_list = []
    def add_node_to_list(node:BinaryTreeNode):
        if(node.left is not None):
            add_node_to_list(node.left)
        if(node.right is not None):
            add_node_to_list(node.right)
        bfs_list.append(node)
        return
    
    add_node_to_list(bt_primary_node)

    for node in bfs_list:
         if (node.left is None or (node.left.has_identical_subtree == True and node.left.value == node.value)) and (node.right is None or (node.right.has_identical_subtree == True and node.right.value == node.value)):
            # leaf or identical tree 
            identical_value_subtree_count += 1
            node.has_identical_subtree = True

    return identical_value_subtree_count

if __name__ == '__main__':
    #  create example tree
    primary_node = BinaryTreeNode(8)
    primary_node.left = BinaryTreeNode(5)
    primary_node.right = BinaryTreeNode(10)
    primary_node.left.left = BinaryTreeNode(5)
    primary_node.left.right = BinaryTreeNode(5)
    primary_node.right.right = BinaryTreeNode(8)
    primary_node.right.left = BinaryTreeNode(10)
    primary_node.right.left.right = BinaryTreeNode(10)

    print(count_subtrees_with_same_values(primary_node))