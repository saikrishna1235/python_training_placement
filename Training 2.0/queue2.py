class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None  # Necessary for O(1) deleteRear operation


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def insertFront(self, val):
        newNode = Node(val)
        if self.isEmpty():
            self.front = self.rear = newNode
        else:
            newNode.next = self.front
            self.front.prev = newNode
            self.front = newNode

    def insertRear(self, val):
        newNode = Node(val)
        if self.isEmpty():
            self.front = self.rear = newNode
        else:
            newNode.prev = self.rear
            self.rear.next = newNode
            self.rear = newNode

    def deleteFront(self):
        if self.isEmpty():
            print("Deque Underflow: Cannot delete from front.")
            return None
        
        temp = self.front
        self.front = self.front.next
        
        if self.front is None:  # Deque became empty
            self.rear = None
        else:
            self.front.prev = None
            
        return temp.val

    def deleteRear(self):
        if self.isEmpty():
            print("Deque Underflow: Cannot delete from rear.")
            return None
        
        temp = self.rear
        self.rear = self.rear.prev
        
        if self.rear is None:  # Deque became empty
            self.front = None
        else:
            self.rear.next = None
            
        return temp.val

    def display(self):
        if self.isEmpty():
            print("Deque is empty.")
            return
        
        current = self.front
        elements = []
        while current:
            elements.append(str(current.val))
            current = current.next
        print(" -> ".join(elements))


# --- Example Usage ---
if __name__ == "__main__":
    dq = Deque()
    
    print("Inserting 10 and 20 at Rear...")
    dq.insertRear(10)
    dq.insertRear(20)
    dq.display()  # Expected: 10 -> 20

    print("\nInserting 5 and 2 at Front...")
    dq.insertFront(5)
    dq.insertFront(2)
    dq.display()  # Expected: 2 -> 5 -> 10 -> 20

    print(f"\nDeleted from Front: {dq.deleteFront()}")  # Expected: 2
    dq.display()  # Expected: 5 -> 10 -> 20

    print(f"\nDeleted from Rear: {dq.deleteRear()}")    # Expected: 20
    dq.display()  # Expected: 5 -> 10
