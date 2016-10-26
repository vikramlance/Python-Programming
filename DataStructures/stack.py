class stack:

    def __init__(self):

        self.elements=[]
        

    def isEmpty(self):
        return self.elements==[]
        	
        
    def size(self):
        return len(self.elements)

    def push(self,ob):
        self.elements.append(ob)
        return self.elements

    def pop (self ):
        return self.elements.pop()

    def peek (self):
        return self.elements[len(self.elements) - 1]
        
st= stack()
print st.isEmpty()

st.push(1)

print st.isEmpty()

print st.size()


st.push(1)

print st.isEmpty()

print st.size()

print st.push(1)
