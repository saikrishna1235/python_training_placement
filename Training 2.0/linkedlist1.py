class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next is not None:
            temp= temp.next
        temp.next=new_node

    def delete(self):
        if self.head is None:
            print("linked list is empty")
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None
    def countNode(self):
        temp=self.head
        count=1
        while temp.next is not None:
            count+=1
            temp=temp.next
        print(count)

    def search(self,data):
        if self.head is None:
            print("linked list is empty")
            return
        temp = self.head
        while temp is not None:
            if temp.data == data:
                print("data found")
                return
            temp = temp.next
        return False

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next


ll = LinkedList()

for _ in range(n):
    value = int(input("Enter data: "))
    
    ll.insert(value)

ll.display()
# ll.delete()
# ll.display()
# ll.countNode()
ll.search(int(input("Enter data to search: ")))