
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 1. Insert at the beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # 2. Insert at the end
    def insert_end(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # 3. Insert at a position (0-based)
    def insert_at_position(self, position, data):
        if position < 0:
            print("Invalid position")
            return

        if position == 0:
            self.insert_beginning(data)
            return

        current = self.head
        index = 0

        while current is not None and index < position:
            current = current.next
            index += 1

        if index != position:
            print("Invalid position")
            return

        if current is None:
            self.insert_end(data)
            return

        new_node = Node(data)
        previous_node = current.prev

        new_node.prev = previous_node
        new_node.next = current
        previous_node.next = new_node
        current.prev = new_node

    # 4. Delete from the beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None

    # 5. Delete from the end
    def delete_end(self):
        if self.tail is None:
            print("List is empty")
            return

        self.tail = self.tail.prev

        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

    # 6. Delete at a position (0-based)
    def delete_at_position(self, position):
        if position < 0:
            print("Invalid position")
            return

        current = self.head
        index = 0

        while current is not None and index < position:
            current = current.next
            index += 1

        if current is None:
            print("Invalid position")
            return

        if current.prev is None:
            self.delete_beginning()
        elif current.next is None:
            self.delete_end()
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

    # 7. Delete by value (first occurrence)
    def delete_value(self, value):
        current = self.head

        while current is not None:
            if current.data == value:
                if current.prev is None:
                    self.delete_beginning()
                elif current.next is None:
                    self.delete_end()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return True

            current = current.next

        return False

    # 8. Search for a value
    def search(self, value):
        current = self.head
        position = 0

        while current is not None:
            if current.data == value:
                return position

            current = current.next
            position += 1

        return -1

    # 9. Display from beginning to end
    def display_forward(self):
        current = self.head

        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next

        print("None")

    # 10. Display from end to beginning
    def display_backward(self):
        current = self.tail

        while current is not None:
            print(current.data, end=" <-> ")
            current = current.prev

        print("None")

    # 11. Count nodes
    def count(self):
        total = 0
        current = self.head

        while current is not None:
            total += 1
            current = current.next

        return total

    # 12. Update a value at a position
    def update(self, position, new_data):
        if position < 0:
            return False

        current = self.head
        index = 0

        while current is not None and index < position:
            current = current.next
            index += 1

        if current is None:
            return False

        current.data = new_data
        return True

    # 13. Reverse the list
    def reverse(self):
        current = self.head

        while current is not None:
            current.prev, current.next = current.next, current.prev
            current = current.prev

        self.head, self.tail = self.tail, self.head

    # 14. Check if list is empty
    def is_empty(self):
        return self.head is None

    # 15. Clear the list
    def clear(self):
        self.head = None
        self.tail = None


# -------- Main program --------

dll = DoublyLinkedList()

dll.insert_beginning(20)
dll.insert_beginning(10)
dll.insert_end(30)
dll.insert_at_position(2, 25)

print("Forward:")
dll.display_forward()

print("Backward:")
dll.display_backward()

print("Number of nodes:", dll.count())
print("Position of 25:", dll.search(25))

dll.update(2, 99)
print("After update:")
dll.display_forward()

dll.delete_beginning()
dll.delete_end()
dll.delete_value(99)

print("After deletions:")
dll.display_forward()

dll.reverse()
print("After reversing:")
dll.display_forward()

print("Is empty?", dll.is_empty())

dll.clear()
print("After clearing:")
dll.display_forward()
