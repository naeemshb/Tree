import gc
from anytree import Node, RenderTree
from operator import or_
node_possibilities = ["op", "num"]

operators = ["plus", "minus", "mul", "div", "min", "max", "OR", "AND", "XOR"]

def create_node (the_name, the_parent, relationship_with_parent):
    a = Node(the_name, parent=the_parent)
    a.left  = None
    a.right = None
    if (the_parent != None):
        assert (relationship_with_parent == "left" or relationship_with_parent == "right")
        if relationship_with_parent == "left":
            the_parent.left = a
        else:
            the_parent.right = a
    return a
    
def create_dummy_tree ():
    root = create_node (["op", 'plus'], None, None)
    a = create_node (["op", 'div'], root, "left")
    b = create_node (["op", 'minus'], root, "right")
    e = create_node (["op", 'max'], b, "left")
    g = create_node (["op", 'min'], e, "left")
    gg = create_node (["num", 4], g, "left")
    ggg = create_node (["num", 5], g, "right")
    h = create_node (["op", 'mul'], e, "right")
    hh = create_node (["num", 2], h, "left")
    hhh = create_node (["num", 3], h, "right")
    f = create_node (["num", 5], b, "right")
    c = create_node (["op", 'XOR'], a, "left")
    cc = create_node (["num", 1], c, "left")
    ccc = create_node (["num", 0], c, "right")
    d = create_node (["op", 'AND'], a, "right")
    dd = create_node (["num", 1], d, "left")
    ddd = create_node (["num", 1], d, "right")
    return root

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

def my_AND_function(a, b):
    return a and b

def my_XOR_function(a, b):
    return (a and not b) or (not a and b)
    # For the case that we don't want logical XOR and it return negative value. Because, in this case it can change the evaluation value negative and it is not true.
    '''
    s = (a * -b) + (-a * b)
    if s < 0:
        return (a and not b) or (not a and b)
    else:
        return s
    '''
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
        case "AND":
            result += my_AND_function(evaluate(mytree.left), evaluate(mytree.right))
        case "XOR":
            result += my_XOR_function(evaluate(mytree.left), evaluate(mytree.right))
    return result


def deallocate (mytree):
    remove_references (mytree)
    mytree = None
    gc.collect()

def remove_references (mytree):
    if (mytree.left != None):
        remove_references (mytree.left)
    if (mytree.right != None):
        remove_references (mytree.right)
    if (mytree.parent != None):
        if (mytree.parent.left == mytree):
            mytree.parent.left = None
        elif mytree.parent.right == mytree:
            mytree.parent.right = None
        else:
            assert 0 == 1 # we should never reach this point
    mytree.parent = None
    mytree.name = []
    mytree.name = None
    mytree = None



def main ():
    copies = []
    print("allocating")
    for i in range(20000):
        root = create_dummy_tree()
        copies.append(root)
    print("deallocating")
    for i in range(20000):
        remove_references(copies[i])
    for i in range(20000):
        copies.pop()
    gc.collect()
    
    #print(RenderTree(root))
    #for pre, fill, node in RenderTree(root):
    #    print("%s%s" % (pre, node.name))
    #print("\n\n evaluating now ...\n\n")
    #value = evaluate(root)
    #print(value)
    #print (" -------------- testing to figure out the data structures -------------- ")
    #deallocate(root)
    #print(" ------------ deallocated memory --------------- ")
    #for pre, fill, node in RenderTree(root):
    #    print("%s%s" % (pre, node.name))
    #print ("---- done ----")
    #print(RenderTree(root))
    #for pre, fill, node in RenderTree(root):
    #      print("%s%s" % (pre, node.name))

if __name__ == "__main__":
    main()
