"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest
leaf node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    return max_depth(root)


def max_depth(node, depth=0):
    """
    :type node: TreeNode
    :type depth: int
    :rtype: int
    """
    if node is None:
        return depth
    return max(max_depth(node.left, depth + 1), max_depth(node.right, depth+1))


def build_tree(tree, nodes, index=0):
    if index >= len(nodes):
        return tree
    if nodes[index] is None:
        return None
    else:
        tree = TreeNode(nodes[index])
        tree.left = build_tree(tree.left, nodes, index + 1)
        tree.right = build_tree(tree.right, nodes, index + 2)
        return tree


if __name__ == '__main__':
    nodes = [3, 9, 20, None, None, 15, 7]
    root = build_tree(None, nodes)
    output = maxDepth(root)
    print(f'output={output}')
