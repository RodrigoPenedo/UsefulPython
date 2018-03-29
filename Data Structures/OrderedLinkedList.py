class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self, value):
        self.value = value

    def setNext(self, n):
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        
        while current != None and not stop:
            if current.getValue() > item:
                stop = True

            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
            
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def size(self):
        current = self.head
        n = 0
        
        while current != None:
            n += 1
            current = current.getNext()

        return n

    def search(self, item):
        current = self.head
        found = False
        
        while current != None and not found:
            if current.getValue() == item:
                found = True
                    
            else:
                current = current.getNext()

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        
        while not found:
            if current.getValue() == item:
                found = True
                
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
            
        else:
            previous.setNext(current.getNext())

    def printlist(self):
        fulllist = ""
        current = self.head
        while current != None:
            fulllist += str(current.getValue()) + " "
            current = current.getNext()

        print(fulllist)
    
    
