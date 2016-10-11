'''
Problem: Find best way to cut a rod of length nn
Given: rod of length nn

Assume that each length rod has a price pipi

Find best set of cuts to get maximum price
Each cut is integer length
Can use any number of cuts, from 0 to n−1n−1
No cost for a cut

Rod Cutting Prices

Example rod lengths and values:
length ii	1	2	3	4	5	6	7	8
price pipi	1	5	8	9	10	17	17	20

'''

#brute force

a= {1:1,2:5,3:8,4:9,5:10,6:17, 7:17,8:20 }

#calculate and save optimum price for given length of rod
