class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def add_beg(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        if self.head is Node:
            print("Linked list is empty")
            return
        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print("None")

    def at_pos(self,data,pos):
        new_node = Node(data)
        if pos == 1:
            self.head = new_node
            return
        else:
            temp = self.head
            for i in range(1,pos-1):
                if temp is None:
                    print("Invalid")
                    return
                temp = temp.next
            if temp is None:
                print("Invalid")
            new_node.next = temp.next
            temp.next = new_node

    
    def delete_node_by_value(self, val):
        if self.head is None:
            print("List is empty")
            return

        # If the head contains the value
        if self.head.data == val:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.data == val:
                temp.next = temp.next.next
                return
            else:
                temp = temp.next

        print("Value not found")

    def search(self,val):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == val:
            print("Element found")
            return
        temp = self.head
        while temp.next is not None:
            if temp.next.data == val:
                print("Element found")
                return
            else:
                temp = temp.next
        print("Element Not found")

    def len_mid(self):
        length = 0
        slow = self.head
        fast = self.head
        temp = self.head
        while temp is not None:
            length+=1
            temp = temp.next
        while fast is not None and fast.next is not None: 
            slow = slow.next
            fast = fast.next.next

        print(slow.data)
        print(length)

    def reverse(self):
        prev = None
        temp = self.head
        while temp is not None:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        self.head = prev

    
    def nth_node_delete(self, n):
        if self.head is None:
            print("Linked list is empty")
            return

        if n <= 0:
            print("Invalid location")
            return
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next
        if n > count:
            print("Invalid location")
            return
        if n == count:
            self.head = self.head.next
            return
        temp = self.head

        for i in range(count - n - 1):
            temp = temp.next
        temp.next = temp.next.next


LL = Linked_List()
LL.add_beg(10)
LL.insert_end(50)
LL.insert_end(60)
LL.add_beg(5)
LL.add_beg(2)
LL.at_pos(6,3)
LL.at_pos(70,7)
LL.delete_node_by_value(10)
LL.search(6)
LL.len_mid()
LL.display()
LL.reverse()
LL.display()
LL.nth_node_delete(2)
LL.display()