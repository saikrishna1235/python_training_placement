class Queue:
    def __init__(self, capacity=5):
        self.queue = []
       



    def in_left(self, data):
        if len(self.queue) < 5:
            self.queue.insert(0, data)
        else:
            print("overflow")
            return

    def in_right(self, data):
        if len(self.queue) < 5:
            self.queue.append(data)
        else:
            print("overflow")
            return

    def re_left(self):
        if len(self.queue) == 0:
            print("Queue underflow")
            return
        return self.queue.pop(0)

    def re_right(self):
        if len(self.queue) == 0:
            print("Queue underflow")
            return
        return self.queue.pop()

    def front(self):
        if not self.queue:
            print("Queue is empty")
            return
        return self.queue[0]

    def rear(self):
        if not self.queue:
            print("Queue is empty")
            return
        return self.queue[-1]


    def display(self):
        print(self.queue)


if __name__ == '__main__':
    q = Queue()
    q.in_right(7)
    q.in_right(8)
    q.in_right(9)
    q.in_right(3)
    q.in_left(18)

    q.display()
    print('Front:', q.front())
    print('Rear:', q.rear())
    print('Dequeued from left:', q.re_left())
    print('Dequeued from right:', q.re_right())
    q.display()