class Queue:
    def __init__(self):
        self.elements=[]

    def size(self):
        return len(self.elements)

    def isEmpty(self):
        return self.elements==[]

    def enque(self, ob):
        self.elements.append(ob)

    def deque(self):
        return self.elements.pop()
