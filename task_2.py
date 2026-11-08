class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def sum_tree(root):
    """Сума всіх значень: вузол + ліве піддерево + праве піддерево."""
    if root is None:
        return 0
    return root.key + sum_tree(root.left) + sum_tree(root.right)


def main():
    root = None
    for key in [50, 30, 70, 20, 40, 60, 80, 10]:
        root = insert(root, key)
    print("Сума значень:", sum_tree(root))
    print("Порожнє дерево:", sum_tree(None))


if __name__ == "__main__":
    main()
