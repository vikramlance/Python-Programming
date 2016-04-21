

import sys
N=int(raw_input().strip())

d={}
for i in range (0,N):
    a=(raw_input())
    m = a.split(' ')
    key =m[0]
    value=m[1]
    #print key
    #print value
    d[key]=value
    #print d

'''
while True:
    try:
        row= raw_input()
        #if row=='':
            #break
        key= row
        if key in d:
            print "%s=%s"%(row,d[key])
        else:
            print "Not found"
    except EOFError:
        sys.exit(0)


'''
while True:
    row= raw_input()
    if row=='':
        break
    #print row
    key= row
    #print key
    if key in d:
        #print d[key]
        print "%s = %s"%(row,d[key])
    else:
        print "Not found"


    
