import uuid

from tree import Node, insert, delete


def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current


root = Node(11)

root = insert(root, 2)
root = insert(root, 20)
root = insert(root, 29)
root = insert(root, 38)
root = insert(root, 47)
root = insert(root, 56)

print(min_value_node(root).val)

delete(root, 2)
print(min_value_node(root).val)
