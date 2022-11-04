from anytree import Node, RenderTree

node_possibilities = ["op", "num"]

operators = ["plus", "minus", "mul", "div", "min", "max", "OR", "AND", "XOR"]

root = Node(["op", "plus"])
a = Node(["op", "div"], parent=root)
b = Node(["op", "minus"], parent=root)
e = Node(["op", 'max'], parent=b)
g = Node(["num", 11], parent=e)
h = Node(["num", 13], parent=e)
f = Node(["num", 4], parent=b)
c = Node(["num", 3], parent=a)
d = Node(["num", 2], parent=a)

root.left = a
root.right = b
a.left = c
a.right = d
b.left = e
b.right = f
e.left = g
e.right = h

#print(RenderTree(root))
for pre, fill, node in RenderTree(root):
      print("%s%s" % (pre, node.name))

val = root.name


print(val)
# print(val[1])

# print(root.children)


def my_plus_function(a, b):
    return a + b

def my_minus_function(a, b):
    return (a - b)

def my_max_function(a, b):

    res = max(a,b)
    return res


def my_div_function(a, b):
    return float(a) / float(b)


def evaluate(mytree):
    if mytree == None:
        print("This should not happen")
        return 0  # throw an exception here; this should not happen

    val = mytree.name
    if val[0] == "num":
        # print("returning a real number now: %f", val[1])
        return val[1]

    result = 0
    match val[1]:
        case "plus":
            result += my_plus_function(evaluate(mytree.left), evaluate(mytree.right))
        case "div":
            result += my_div_function(evaluate(mytree.left), evaluate(mytree.right))
        case "minus":
            result += my_minus_function(evaluate(mytree.left), evaluate(mytree.right))
        case "max":
            result += my_max_function(evaluate(mytree.left), evaluate(mytree.right))
    return result


print("\n\n evaluating now ...\n\n")

value = evaluate(root)

print(value)
