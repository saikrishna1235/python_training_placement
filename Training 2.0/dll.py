
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 1. Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # 2. Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.head = self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    # 3. Insert at a given position (1-based)
    def insert_at_position(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            self.insert_at_beginning(data)
            return

        temp = self.head

        for _ in range(pos - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        if temp == self.tail:
            self.insert_at_end(data)
            return

        new_node = Node(data)
        new_node.next = temp.next
        new_node.prev = temp

        temp.next.prev = new_node
        temp.next = new_node

    # 4. Delete from beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.head = self.head.next
        self.head.prev = None

    # 5. Delete from end
    def delete_from_end(self):
        if self.tail is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.tail = self.tail.prev
        self.tail.next = None

    # 6. Delete at a given position (1-based)
    def delete_at_position(self, pos):
        if pos < 1 or self.head is None:
            print("Invalid position or empty list")
            return

        if pos == 1:
            self.delete_from_beginning()
            return

        temp = self.head

        for _ in range(pos - 1):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        if temp == self.tail:
            self.delete_from_end()
            return

        temp.prev.next = temp.next
        temp.next.prev = temp.prev

    # 7. Delete first occurrence of a value
    def delete_by_value(self, value):
        temp = self.head

        while temp is not None and temp.data != value:
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        if temp == self.head:
            self.delete_from_beginning()
        elif temp == self.tail:
            self.delete_from_end()
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev

    # 8. Search for a value (returns 1-based position)
    def search(self, value):
        temp = self.head
        pos = 1

        while temp is not None:
            if temp.data == value:
                return pos
            temp = temp.next
            pos += 1

        return -1

    # 9. Display forward
    def display_forward(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    # 10. Display backward
    def display_backward(self):
        temp = self.tail

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")

    # 11. Find length
    def length(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        return count

    # 12. Get value at a given position (1-based)
    def get_at_position(self, pos):
        if pos < 1:
            return None

        temp = self.head

        for _ in range(pos - 1):
            if temp is None:
                return None
            temp = temp.next

        if temp is None:
            return None

        return temp.data

    # 13. Reverse the list in place
    def reverse(self):
        current = self.head

        while current is not None:
            current.prev, current.next = current.next, current.prev
            current = current.prev

        self.head, self.tail = self.tail, self.head


# Example usage
dll = DoublyLinkedList()

dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_end(40)

print("Forward:")
dll.display_forward()

print("Backward:")
dll.display_backward()

print("Length:", dll.length())
print("Position of 30:", dll.search(30))

dll.insert_at_beginning(5)
dll.insert_at_position(25, 4)

print("After insertions:")
dll.display_forward()

dll.delete_from_beginning()
dll.delete_from_end()
dll.delete_at_position(2)
dll.delete_by_value(30)

print("After deletions:")
dll.display_forward()

dll.reverse()
print("After reversing:")
dll.display_forward()
