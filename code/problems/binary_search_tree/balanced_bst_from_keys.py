# Construct a balanced BST from the given keys
# Given an unsorted integer array that represents binary search tree (BST) keys,
# construct a height-balanced BST from it. 
# For each node of a height-balanced tree,
# the difference between its left and right subtree height is at most 1.

# For example,

# Input: keys = [15, 10, 20, 8, 12, 16, 25] 
# Output:        
#                   15 
#                   /    \  
#                   10     20
#                   /  \   /  \
#                   8   12 16  25 
# OR        
#                   12     
#                   /    \    
#                   10    20   
#                   /     /  \  
#                   8     16  25       
#                          /      
#                          15 
# OR Any other possible representation.

import math

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left:BinaryTreeNode = None
        self.right:BinaryTreeNode = None


def balanced_bst_from_list(list: list):
    list.sort() # nlog(n)

    def add_node(sorted_list):
        if sorted_list == None or len(sorted_list) == 0:
            # should not reach this case
            return None
        elif len(sorted_list) == 1:
            return BinaryTreeNode(sorted_list[0])
        else:
            median = math.floor(len(sorted_list)/2)
            new_node = BinaryTreeNode(sorted_list[median])
            new_node.left = add_node(sorted_list[0:median])
            new_node.right = add_node(sorted_list[median+1:len(sorted_list)])
            return new_node
        
    return add_node(list)


def print_binary_tree(primary_tree_node: BinaryTreeNode):
    depth_arrays = {}
    def process_node(node:BinaryTreeNode, depth):
        # build arrays at each depth
        if node is not None and node.value is not None:
            depth_arrays.setdefault(depth, []).append(str(node.value) + ' ')
            if node.left is not None:
                process_node(node.left, depth+1)
            else:
                depth_arrays.setdefault(depth+1, []).append(' ')
            if node.right is not None:
                process_node(node.right, depth+1)
            else:
                depth_arrays.setdefault(depth+1, []).append(' ')
    
    process_node(primary_tree_node, 0)

    for depth,row in depth_arrays.items():
        top_str = ''
        bottom_str = ''
        for key,node_val in enumerate(row):
            if int(key) % 2 == 0:
                # even = |
                if node_val != ' ':
                    top_str += ('|' + ' '*len(str(node_val)))
                else:
                    top_str += '  '
                bottom_str += (str(node_val) + ' ')
            else:
                # odd = \
                if node_val != ' ':
                    top_str += ('\\' + ' '*len(str(node_val)))
                else:
                    top_str += '  '
                bottom_str += (str(node_val) + ' ')
        print(top_str)
        print(bottom_str)



if __name__ == '__main__':
    balanced_tree_primary_node = balanced_bst_from_list([15, 10, 20, 8, 12, 16, 25, 99, 100, 101])
    print_binary_tree(balanced_tree_primary_node)