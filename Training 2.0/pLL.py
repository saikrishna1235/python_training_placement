class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def display(self):
        temp = self.head
        if temp is None:
            print("Linked list is empty")
            return
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print("None")

    def insert_at_beg(self,data):
        new_node = Node(data)

        new_node.next=self.head
        self.head=new_node
    def insert_end(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next 
        temp.next=new_node
    def insert_at_pos(self,data,pos):
        new_node = Node(data)
        if pos == 1:
            new_node.next=self.head
            self.head=new_node
            return
        temp = self.head
        for i in range(1,pos-1):
            if temp is None:
                print("Invalid position")
                return 
            temp = temp.next
        if temp is None:
            print("invalid")
            return 
        new_node.next = temp.next
        temp.next=new_node
    def delete_beg(self):
        if self.head is None:
            print("Empty list")
            return 
        self.head = self.head.next
    def delete_end(self):
        if self.head is None:
            print("Empty list")
            return 
        if self.head.next is None:
            self.head = None
            return 
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
    
ll = LinkedList()

ll.display()
ll.insert_end(10)
ll.insert_at_beg(20)
ll.display()