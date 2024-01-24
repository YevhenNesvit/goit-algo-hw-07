import uuid

from tree import Node, insert


def sum_values(root):
    if not root:
        return 0
    return root.val + sum_values(root.left) + sum_values(root.right)


root = Node(11)

root = insert(root, 2)
root = insert(root, 47)
root = insert(root, 20)
root = insert(root, 29)
root = insert(root, 56)
root = insert(root, 38)


print(sum_values(root))
