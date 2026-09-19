class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert node
    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        self.insert_node(self.root, new_node)

    def insert_node(self, root, new_node):
        if new_node.data < root.data:
            if root.left is None:
                root.left = new_node
            else:
                self.insert_node(root.left, new_node)

        else:
            if root.right is None:
                root.right = new_node
            else:
                self.insert_node(root.right, new_node)

    # Inorder Traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Preorder Traversal
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder Traversal
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    # Search
    def search(self, root, data):
        if root is None:
            return False

        if root.data == data:
            return True

        if data < root.data:
            return self.search(root.left, data)

        return self.search(root.right, data)


# Create Binary Tree
tree = BinaryTree()

# Insert elements
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)

# Traversals
print("Inorder:")
tree.inorder(tree.root)

print("\nPreorder:")
tree.preorder(tree.root)

print("\nPostorder:")
tree.postorder(tree.root)

# Search
print("\nSearch 40:", tree.search(tree.root, 40))
print("Search 90:", tree.search(tree.root, 90))