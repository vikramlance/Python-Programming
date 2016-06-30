'''
Task 
Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

Input Format

The first line of input contains M an integer, . 
The second line contains M space-separated integers. 
The third line contains an integer, N. 
The fourth line contains N space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.

Sample Input

4
2 4 5 9
4
2 4 11 12
Sample Output

5
9
11
12
'''


a=raw_input().strip()
b= map(int,raw_input().strip().split(' '))
c=raw_input().strip()
d=map(int,raw_input().strip().split(' '))

#d.sort()
#print d

f=list()      
for i in b:
    for k in d:
        x=0
        if k==i:
            x=1
            break
    if x==0:
        f.append(i)

for j in d:
    for m in b:
        y=0
        if m==j:
            y=1
            break
    if y==0:
        f.append(j)
        
f=list(set(f))
f.sort()
for z in f:
    print z
            
        
