class Dequeue:
    def __init__(self):
        self.items = []

    def Empty(self):
        return self.items == []

    def addFront(self, item):
        self.items.insert(0,item)

    def add(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)

    def removeBack(self):
        return self.items.pop()

    def Length(self):
        return len(self.items)

    def PeekFront(self):
        return self.items[0]

    def PeekBack(self):
        return self.items[-1]
        
    def Clear(self):
        self.items = []
