class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.data,end=" ")
        if self.right is not None:
            self.right.inorder()
root = Node(1)
root.left = Node(2)
root.right = Node(3)


root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

root.inorder()