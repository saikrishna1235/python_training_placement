class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def insert_at_begining(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node


    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def insert_at_given_position(self,data,pos):
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for i in range(1,pos-1):
            if temp is None:
                print("Position not valid")
                return
            temp = temp.next
        if temp is None:
            print("Position not valid")
        new_node.next = temp.next
        temp.next = new_node

    def delete_from_beg(self,val):
        if self.head is None:
            print("No elements to delete")
            return
        if self.head.data == val:
            self.head = self.head.next
            return
        temp = self.head

    def search(self,key):
        temp = self.head
        while temp.next is not None:
            if temp.data == key:
                print("Found")
                return
            else:
                temp = temp.next
    def length(self,count):
        temp = self.head 
        while temp is not None:
            temp = temp.next
            count+=1
        print(count)
    def reverse(self):
        pre
LL = Linked_List()
LL.append(10)
LL.append(20)
LL.append(30)
LL.append(40)
# LL.insert_at_begining(5)
# LL.insert_at_end(50)
# LL.insert_at_end(60)
# LL.insert_at_given_position(15,3)
# LL.delete_from_beg(30)
# LL.display()
# LL.search(110)
LL.length(0)
LL.display()