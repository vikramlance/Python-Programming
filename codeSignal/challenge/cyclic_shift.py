"""

"""

def arrayShift(elements):
    len_elements = len(elements)
    flag = True
    for i in range(len_elements -1):
        if elements[i] > elements[i+1] and elements[i] != len_elements:
            flag = False
        if  elements[i+1] - elements[i] > 1:
            flag = False
    
    if flag:
        return True
    
    if not flag:
        for i in range(len_elements -1):
            if elements[i] < elements[i+1] and elements[i+1] != len_elements:
                return False
            if elements[i] - elements[i+1] > 1:
                return False
        return True
    
    
    
            
        
        


    
    
    
            
        
        



