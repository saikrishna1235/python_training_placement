class LL:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_beg(self, data):
        new_node = LL(data)

        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = LL(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Insert at a specific position
    def insert_pos(self, data, pos):
        new_node = LL(data)

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(1, pos - 1):
            if temp is None:
                print("Position not found")
                return
            temp = temp.next

        if temp is None:
            print("Position not found")
            return

        new_node.next = temp.next
        temp.next = new_node

    # Display
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Create linked list
ll = LinkedList()

# Insert at beginning
ll.insert_beg(20)
ll.insert_beg(10)

# Insert at end
ll.insert_end(30)
ll.insert_end(40)

# Insert at position
ll.insert_pos(25, 3)

# Display
ll.display()