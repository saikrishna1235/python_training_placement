class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head=None
    def add_end(self,data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new
    def find_mid_point(self):
        if self.head is None:
            return None
        p1=self.head
        p2=self.head
        position = 1
        while p1.next.next :
            p2 = p2.next
            p1=p1.next.next
            position+=1
        return position,p2.data
    def add_beg(self,data):
        obj = Node(data)
        if self.head is None:
            self.head = obj
            return
        obj.next = self.head
        self.head = obj
    def display(self):
        itr = self.head
        while itr:
            print(itr.data,end ="-->")
            itr = itr.next
ll=LinkedList()
ll.add_end(50)
ll.add_end(150)
ll.add_end(250)
ll.add_end(350)
ll.add_end(450)
ll.add_beg(10)
ll.find_mid_point()
ll.display()

middle = ll.find_mid_point()
if middle is None :
    print("Linked list is empty")
else:
    pos,value=middle
    print(f"Middle position : {pos}, middle value :{value}")