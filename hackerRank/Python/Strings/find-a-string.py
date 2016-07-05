a=raw_input()
b=raw_input()

count=0
for i in range(0,len(a)-len(b)+1):
    
    if a[i:i+len(b)]== b:
        count=count+1
        #print count
print count
