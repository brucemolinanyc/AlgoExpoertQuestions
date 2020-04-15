"""
Write a funciton that takes in a Binary Search Tree (BST) and a target integer value and returns the closes value to that
target value contained in the BST.

You can assume that there will only be one closest value.

Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if and 
only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is 
less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves
or None/Null
"""

# recursive solution 
def findClosestValueInBST(tree, target):
    return findClosestValue(tree, target, float("inf"))


def findClosestValue(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBST(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBST(tree.right, target, closest)
    else: 
        return closest




#iterative solution
def findClosestValue(tree, target, closest):
    currentNode = tree 
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right 
        else: 
            return closest

