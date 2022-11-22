from anytree import Node, RenderTree
class Node:

	def __init__(self, Node):
		self.Node = Node
		self.left = None
		self.right = None


def Depth(node):

	if node is None:
		return 0

	else:
		leftdepth = Depth(node.left)
		rightdepth = Depth(node.right)
		#return max(leftdepth, rightdepth) +1

		if (leftdepth > rightdepth):
			return leftdepth+1
		else:
			return rightdepth+1



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)

#for pre, fill, node in RenderTree(root):
#   print("%s%s" % (pre, Node.name))
print("Height of tree is %d" % (Depth(root)))
print("Height of tree is %d" % (Depth(root.left)))
print("Height of tree is %d" % (Depth(root.left.right)))
print("Height of tree is %d" % (Depth(root.left.right.right)))



