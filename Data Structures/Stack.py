class Stack:
    def __init__(self):
        self.items = []
        
    def Empty(self):
        return self.items == []
    
    def Push(self, item):
        self.items.append(item)
        
    def Pop(self):
        return self.items.pop()

    def Peek(self):
        return self.items[-1]
    
    def Clear(self):
        self.items = []
