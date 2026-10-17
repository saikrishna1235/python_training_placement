# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Display / Traverse
    def display(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 2. Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 3. Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    # 4. Insert at a specific position
    def insert_position(self, data, position):
        new_node = Node(data)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(1, position - 1):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # 5. Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    # 6. Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        # Only one node
        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

    # 7. Delete from a specific position
    def delete_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position == 1:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(1, position - 1):
            if temp.next is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp.next is None:
            print("Invalid position")
            return

        temp.next = temp.next.next

    # 8. Search
    def search(self, key):
        temp = self.head
        position = 1

        while temp:
            if temp.data == key:
                print(key, "found at position", position)
                return

            temp = temp.next
            position += 1

        print(key, "not found")

    # 9. Count nodes
    def count(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count

    # 10. Reverse linked list
    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous


# -------------------------------
# Main Program
# -------------------------------

ll = LinkedList()

# Insert operations
ll.insert_beginning(20)
ll.insert_beginning(10)
ll.insert_end(30)
ll.insert_end(40)

print("Original List:")
ll.display()

# Insert at position
ll.insert_position(25, 3)

print("\nAfter inserting 25 at position 3:")
ll.display()

# Search
print("\nSearching:")
ll.search(30)
ll.search(100)

# Count
print("\nNumber of nodes:", ll.count())

# Delete beginning
ll.delete_beginning()

print("\nAfter deleting from beginning:")
ll.display()

# Delete end
ll.delete_end()

print("\nAfter deleting from end:")
ll.display()

# Delete position
ll.delete_position(2)

print("\nAfter deleting position 2:")
ll.display()

# Reverse
ll.reverse()

print("\nAfter reversing:")
ll.display()