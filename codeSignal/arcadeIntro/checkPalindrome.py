

def checkPalindrome(inputString):
    from collections import deque 
    
    stack = deque()
    
    reversed_input = ''
    
    for i in inputString:
        stack.append(i)
        
    for j in range(len(inputString)):
        
        reversed_input = reversed_input + stack.pop()
        
    if inputString == reversed_input:
        return True
    else:
        return False
        
    
    

print(checkPalindrome('abaaa'))