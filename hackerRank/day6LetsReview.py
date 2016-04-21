'''
Task 
Given a string, S, of length N that is indexed from 0 to N−1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.

Input Format

The first line contains an integer, T (the number of test cases). 
Each line ii of the T subsequent lines contain a String, S.

Sample Input

2
Hacker
Rank
Sample Output

Hce akr
Rn ak
'''


T=int(raw_input())

for i in range (0,T):
    s=raw_input()
    p=list(s)
    e=''
    o=''
    for j in range (0,len(p),2):
    
        e= e+ p[j]
    for k in range (1,len(p),2):
        o= o +p[k] 
    print "%s %s" %(e,o)
            
