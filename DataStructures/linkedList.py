'''
LInked list implementation in python
'''
class Node:
    def __init__(self, data=None, next_node=None):
        self.data=data
        self.next_node=next_node
    def getdata(self):
        return self.data
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        self.next_node=new_next
        
class LinkedList:
    def init(self,head=None):
        self.head=head
    def insert(self,data):
        new_node= Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    def size(self):
        count=0
        current=self.head
        while current:
            count +=1
            current=current.get_next()
        return count
    def search(self,data):
        current=self.head
        found=False  
        while data<>self.data:
            current=current.get_next()
        retunr Node(data)
