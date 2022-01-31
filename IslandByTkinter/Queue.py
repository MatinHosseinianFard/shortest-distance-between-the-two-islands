class Queue:

    def __init__(self, capacity):
        self.front = 0
        self.size = 0
        self.rear = capacity - 1
        self.Q = [None] * capacity
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def EnQueue(self, item):
        if self.isFull():
            print("Full")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1

    def DeQueue(self):
        if self.isEmpty():
            print("Empty")
            return

        pop = self.Q[self.front]
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1
        return pop

    def Size(self):
        return self.size
