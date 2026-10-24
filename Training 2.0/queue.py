class Queue:
    def __init__(self):
        self.SIZE = 100
        self.queue = [0] * self.SIZE
        self.front = -1
        self.rear = -1

    def isFull(self):
        return self.rear == self.SIZE - 1

    def isEmpty(self):
        return self.front == -1 or self.front > self.rear

    def enqueue(self, val):
        if self.isFull():
            print("Queue is full")
            return
        
        # If the queue is completely empty, initialize front to 0
        if self.front == -1:
            self.front = 0
            
        self.rear += 1
        self.queue[self.rear] = val

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        
        val = self.queue[self.front]
        self.front += 1
        return val

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        
        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")
        print()

# --- Execution ---
e = Queue()
e.enqueue(10)
e.enqueue(20)
e.enqueue(30)

print("Queue elements after enqueuing 10, 20, 30:")
e.display()

print(f"Dequeued element: {e.dequeue()}")

print("Queue elements after one dequeue operation:")
e.display()
