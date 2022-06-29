from numpy import number
from binarytree import Node
from collections import deque
from typing import List



def text_to_list(file_name:str)-> List[List[int]]:
    """
    Converts numbers in text file in triangle to
    lists of lists.
    """

    with open(f"./static/{file_name}", "r") as nfile:
        number_list = [list(map(int,(line.strip().split()))) for line in nfile.readlines()]
        
    return number_list
    

def max_sum(arr:List[List[int]])-> int:
    result_arr = arr[0]
    for row in arr[1:]:
        new_result_arr = []
        for x,value in enumerate(row):
            if x==0:
                # 1st element of row
                new_result_arr += [value+result_arr[0]]
            elif x==len(row)-1:
                # last element of row
                new_result_arr += [value + result_arr[-1]]
            else:
                # mid-elements of row
                new_result_arr += [value+max(result_arr[x],result_arr[x-1])]
            
        result_arr = new_result_arr
    return result_arr

# def list_to_tree(numbers):
#     tree = Node(numbers[0])
#     for n in range(1, len(numbers[1:])):
#         tree.insert(numbers[n])
#     return tree

number_list=text_to_list('maxpathsum.txt')
print(number_list)
# tree=list_to_tree(number_list)
# print()
# print(tree)

# def isLeaf(node):
#     return node.left is None and node.right is None

# def printRootToLeafPaths(node, path):
 
#     # base case
#     if node is None:
#         return
 
#     # include the current node to the path
#     path.append(node.data)
 
#     # if a leaf node is found, print the path
#     if isLeaf(node):
#         print(list(path))
 
#     # recur for the left and right subtree
#     printRootToLeafPaths(node.left, path)
#     printRootToLeafPaths(node.right, path)
 
#     # backtrack: remove the current node after the left, and right subtree are done
#     path.pop()
# def printRootToLeafPath(root):
 
#     # list to store root-to-leaf path
#     path = deque()
#     printRootToLeafPaths(root, path)

# printRootToLeafPath(tree)