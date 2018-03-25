class Queue:
    def __init__(self):
        self.items = []

    def Empty(self):
        return self.items == []

    def Enqueue(self, item):
        self.items.insert(0,item)

    def Dequeue(self):
        return self.items.pop()

    def Length(self):
        return len(self.items)
        
    def Clear(self):
        self.items = []
