class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def add_beg(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def add_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def add_pos(self,data,pos):
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return
        else:
            temp = self.head
            for i in range(1,pos-1):
                if temp is None:
                    print("Position not found")
                    return 
                temp = temp.next
            if temp is None:
                print("Position not found")
                return 
            new_node.next = temp.next
            temp.next = new_node
            
    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

LL  = linked_list()
LL.add_beg(10)
LL.add_beg(20)
LL.add_end(30)
LL.add_end(40)
LL.add_pos(5,1)
LL.display()