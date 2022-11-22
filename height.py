#from anytree import Node, RenderTree
'''
def find_depth(tree, node):
    if node is None or tree is None:
        return 0

    if tree == node:
        return 1

    left = find_depth(tree.left, node)
    if left != 0:
        return 1 + left
    right = find_depth(tree.right, node)
    if right != 0:
        return 1 + right

    return 0
'''

def max_depth(t,value):
    if t == None:
        return -1
    left = max_depth(t.left, value)
    right = max_depth(t.right, value)
    if t.value == value or left > -1 or right > -1: # <<<<
        return 1 + max(left,right)
    else:
        return max(left,right) # This is always -1
class TN:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left  = left
        self.right = right


tree4 = TN(2)
tree3 = TN(3, left=None, right=tree4)
tree2 = TN(2)
tree1 = TN(1, left=tree2, right=tree3)
print(max_depth(tree1, 2))

#find_depth(tree, 5)