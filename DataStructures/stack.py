class stack:

    def __init__(self):

        pass

    def isEmpty(self,inputStack):
        if inputStack==None:
            return True
        else:
            return False
    def size(self,inputStack):
        return len(inputStack)

    def pushObject(self, inputStack, ob):
        inputStack.append(ob)
