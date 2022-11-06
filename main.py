from anytree import Node, RenderTree
from operator import or_
node_possibilities = ["op", "num"]

operators = ["plus", "minus", "mul", "div", "min", "max", "OR", "AND", "XOR"]

root = Node(["op", "plus"])
a = Node(["op", "div"], parent=root)
b = Node(["op", "minus"], parent=root)
e = Node(["op", 'max'], parent=b)
g = Node(["op", 'min'], parent=e)
gg = Node(["num", 4], parent=g)
ggg = Node(["num", 5], parent=g)
h = Node(["op", 'mul'], parent=e)
hh = Node(["num", 2], parent=h)
hhh = Node(["num", 3], parent=h)
f = Node(["op", 'OR'], parent=b)
ff = Node(["num", 4], parent=f)
fff= Node(["num", 1], parent=f)
c = Node(["op", 'XOR'], parent=a)
cc = Node(["num", 1], parent=c)
ccc = Node(["num", 3], parent=c)
d = Node(["num", 2], parent=a)


root.left = a
root.right = b
a.left = c
a.right = d
b.left = e
b.right = f
e.left = g
e.right = h
f.left = ff
f.right = fff
c.left = cc
c.right = ccc
g.left = gg
g.right = ggg
h.left = hh
h.right = hhh

#print(RenderTree(root))
for pre, fill, node in RenderTree(root):
      print("%s%s" % (pre, node.name))

val = root.name


print(val)
# print(val[1])

# print(root.children)


def my_plus_function(a, b):
    return a + b

def my_mul_function(a, b):
    return (a * b)

def my_minus_function(a, b):
    return (a - b)

def my_max_function(a, b):
    res = max(a,b)
    return res

def my_min_function(a, b):
    res = min(a,b)
    return res

def my_OR_function(a, b):
    return a or b

def my_XOR_function(a, b):
    return (a and not b) or (not a and b)

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
        case "mul":
            result += my_mul_function(evaluate(mytree.left), evaluate(mytree.right))
        case "max":
            result += my_max_function(evaluate(mytree.left), evaluate(mytree.right))
        case "min":
            result += my_min_function(evaluate(mytree.left), evaluate(mytree.right))
        case "OR":
            result += my_OR_function(evaluate(mytree.left), evaluate(mytree.right))

        case "XOR":
            result += my_XOR_function(evaluate(mytree.left), evaluate(mytree.right))
    return result


print("\n\n evaluating now ...\n\n")

value = evaluate(root)

print(value)
