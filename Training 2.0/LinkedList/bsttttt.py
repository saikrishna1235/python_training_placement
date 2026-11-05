class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class BST:
  def __init__(self):
    self.root=None
  def insert(self,root,val):
    newNode=Node(val)
    if root is None:
      root = newNode
      return root
    if val<root.data:
      root.left=self.insert(root.left,val)
    else:
      root.right=self.insert(root.right,val)

tree=BST()
while True:
  val=int(input())
  if val==-1:
    break