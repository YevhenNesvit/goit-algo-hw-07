import uuid

from tree import Node, insert, delete


def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current


root = Node(11)

root = insert(root, 2)
root = insert(root, 47)
root = insert(root, 20)
root = insert(root, 29)
root = insert(root, 56)
root = insert(root, 38)


print(max_value_node(root).val)

delete(root, 56)
print(max_value_node(root).val)
