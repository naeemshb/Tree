import gc
from anytree import Node, RenderTree
from operator import or_

node_possibilities = ["op", "num"]
operators = ["plus", "minus", "mul", "div", "min", "max", "OR", "AND", "XOR"]
relations = {'root': [],
             'a': ['root'],
             'b': ['root'],
             'e': ['root', 'b'],
             'g': ['root', 'b', 'e'],
             'gg': ['root', 'b', 'e', 'g'],
             'ggg': ['root', 'b', 'e', 'g'],
             'h': ['root', 'b', 'e'],
             'hh': ['root', 'b', 'e', 'h'],
             'hhh': ['root', 'b', 'e', 'h'],
             'f': ['root', 'b'],
             'c': ['root', 'a'],
             'cc': ['root', 'a', 'c'],
             'ccc': ['root', 'a', 'c'],
             'd': ['root', 'a'],
             'dd': ['root', 'a', 'd'],
             'ddd': ['root', 'a', 'd']}


def create_node(the_name, the_parent, relationship_with_parent):
    a = Node(the_name, parent=the_parent)
    a.left = None
    a.right = None
    if (the_parent != None):
        assert (relationship_with_parent == "left" or relationship_with_parent == "right")
        if relationship_with_parent == "left":
            the_parent.left = a
        else:
            the_parent.right = a
    return a


def update_heights(height_dict, node_name):
    for i, p in enumerate(relations[node_name]):
        if height_dict[p] < len(relations[node_name][i:]):
            height_dict[p] += 1

    return height_dict


def create_dummy_tree():
    all_heights = {}
    heights = {}
    for i in relations.keys():
        heights[i]=0


    root = create_node(["op", 'plus'], None, None)
    heights = update_heights(heights, 'root')
    all_heights['root'] = heights.copy()

    a = create_node(["op", 'div'], root, "left")
    heights = update_heights(heights, 'a')
    all_heights['a'] = heights.copy()

    b = create_node(["op", 'minus'], root, "right")
    heights = update_heights(heights, 'b')
    all_heights['b'] = heights.copy()

    e = create_node(["op", 'max'], b, "left")
    heights = update_heights(heights, 'e')
    all_heights['e'] = heights.copy()

    g = create_node(["op", 'min'], e, "left")
    heights = update_heights(heights, 'g')
    all_heights['g'] = heights.copy()

    gg = create_node(["num", 4], g, "left")
    heights = update_heights(heights, 'gg')
    all_heights['gg'] = heights.copy()

    ggg = create_node(["num", 5], g, "right")
    heights = update_heights(heights, 'ggg')
    all_heights['ggg'] = heights.copy()

    h = create_node(["op", 'mul'], e, "right")
    heights = update_heights(heights, 'h')
    all_heights['h'] = heights.copy()

    hh = create_node(["num", 2], h, "left")
    heights = update_heights(heights, 'hh')
    all_heights['hh'] = heights.copy()

    hhh = create_node(["num", 3], h, "right")
    heights = update_heights(heights, 'hhh')
    all_heights['hhh'] = heights.copy()

    f = create_node(["num", 5], b, "right")
    heights = update_heights(heights, 'f')
    all_heights['f'] = heights.copy()

    c = create_node(["op", 'XOR'], a, "left")
    heights = update_heights(heights, 'c')
    all_heights['c'] = heights.copy()

    cc = create_node(["num", 1], c, "left")
    heights = update_heights(heights, 'cc')
    all_heights['cc'] = heights.copy()

    ccc = create_node(["num", 0], c, "right")
    heights = update_heights(heights, 'ccc')
    all_heights['ccc'] = heights.copy()

    d = create_node(["op", 'AND'], a, "right")
    heights = update_heights(heights, 'd')
    all_heights['d'] = heights.copy()

    dd = create_node(["num", 1], d, "left")
    heights = update_heights(heights, 'dd')
    all_heights['dd'] = heights.copy()

    ddd = create_node(["num", 1], d, "right")
    heights = update_heights(heights, 'ddd')
    all_heights['ddd'] = heights.copy()
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))
    return root, heights, all_heights


def my_plus_function(a, b):
    return a + b


def my_mul_function(a, b):
    return (a * b)


def my_minus_function(a, b):
    return (a - b)


def my_max_function(a, b):
    res = max(a, b)
    return res


def my_min_function(a, b):
    res = min(a, b)
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

    if val[1] == "plus":
        result += my_plus_function(evaluate(mytree.left), evaluate(mytree.right))
    elif val[1] == "div":
        result += my_div_function(evaluate(mytree.left), evaluate(mytree.right))
    elif val[1] == "minus":
        result += my_minus_function(evaluate(mytree.left), evaluate(mytree.right))
    elif val[1] == "mul":
        result += my_mul_function(evaluate(mytree.left), evaluate(mytree.right))
    elif val[1] == "max":
        result += my_max_function(evaluate(mytree.left), evaluate(mytree.right))
    elif val[1] == "min":
        result += my_min_function(evaluate(mytree.left), evaluate(mytree.right))
    elif val[1] == "OR":
        result += my_OR_function(evaluate(mytree.left), evaluate(mytree.right))
    elif val[1] == "AND":
        result += my_AND_function(evaluate(mytree.left), evaluate(mytree.right))
    elif val[1] == "XOR":
        result += my_XOR_function(evaluate(mytree.left), evaluate(mytree.right))

    return result


def deallocate(mytree):
    remove_references(mytree)
    mytree = None
    gc.collect()


def remove_references(mytree):
    if (mytree.left != None):
        remove_references(mytree.left)
    if (mytree.right != None):
        remove_references(mytree.right)
    if (mytree.parent != None):
        if (mytree.parent.left == mytree):
            mytree.parent.left = None
        elif mytree.parent.right == mytree:
            mytree.parent.right = None
        else:
            assert 0 == 1  # we should never reach this point
    mytree.parent = None
    mytree.name = []
    mytree.name = None
    mytree = None


def main():
    copies = []
    print("allocating")
    for i in range(20000):
        root, h, hr = create_dummy_tree()
        copies.append(root)
    print("deallocating")
    for i in range(20000):
        remove_references(copies[i])
    for i in range(20000):
        copies.pop()
    gc.collect()

    # print(RenderTree(root))
    # for pre, fill, node in RenderTree(root):
    #    print("%s%s" % (pre, node.name))
    # print("\n\n evaluating now ...\n\n")
    # value = evaluate(root)
    # print(value)
    # print (" -------------- testing to figure out the data structures -------------- ")
    # deallocate(root)
    # print(" ------------ deallocated memory --------------- ")
    # for pre, fill, node in RenderTree(root):
    #    print("%s%s" % (pre, node.name))
    # print ("---- done ----")
    # print(RenderTree(root))
    # for pre, fill, node in RenderTree(root):
    #      print("%s%s" % (pre, node.name))

# #
# if __name__ == "__main__":
#     main()
r,h,ah = create_dummy_tree()
print(h)
