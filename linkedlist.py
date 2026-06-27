class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_end(self,data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new
    def add_beg(self,data):
        new = Node(data)
        new.next = self.head
        self.head = new
    # Add element at given position (1-based indexing)
    def add_at_position(self,pos,data):
        if pos <= 1:
            self.add_beg(data)
            return
        new = Node(data)
        itr = self.head
        count = 1
        while itr and count < pos - 1:
            itr = itr.next
            count += 1
        if itr is None:
            print("Position out of range")
            return
        new.next = itr.next
        itr.next = new
    # Remove first node
    def delete_beg(self):
        if self.head is None:
            return None
        value = self.head.data
        self.head = self.head.next
        return value
    # Remove last node
    def delete_last_node(self):
        if self.head is None:
            return None
        if self.head.next is None:
            value = self.head.data
            self.head = None
            return value
        itr = self.head
        while itr.next.next:
            itr = itr.next
        value = itr.next.data
        itr.next = None
        return value
    def display(self):
        itr = self.head
        while itr:
            print(itr.data,end=" --> ")
            itr = itr.next
        print("None")
# Driver Code
ll = LinkedList()
ll.add_end(50)
ll.add_end(150)
ll.add_end(250)
ll.add_end(350)
ll.add_end(450)
ll.add_end(150)
ll.add_end(250)
print("Original Linked List")
ll.display()
print("\nAdd at position 3")
ll.add_at_position(3,999)
ll.display()
print("\nDelete from beginning")
print("Deleted :",ll.delete_beg())
ll.display()
print("\nDelete from end")
print("Deleted :",ll.delete_last_node())
ll.display()
print("\nRemove any 2 nodes")
ll.delete_node(150)
ll.delete_node(350)
ll.display()
print("\nMiddle Element :",ll.find_mid_point())
print("\nDuplicates :",ll.find_duplicates())
print("\nLoop Present :",ll.detect_loop())
print("\nReverse Linked List")
ll.reverse_ll()
ll.display()