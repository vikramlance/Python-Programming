"""
Given numBottles full water bottles, you can exchange numExchange empty water bottles for one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Return the maximum number of water bottles you can drink.

 

Example 1:



Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.
Example 2:



Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
Number of water bottles you can drink: 15 + 3 + 1 = 19.
Example 3:

Input: numBottles = 5, numExchange = 5
Output: 6
Example 4:

Input: numBottles = 2, numExchange = 3
Output: 2
 

Constraints:

1 <= numBottles <= 100
2 <= numExchange <= 100

questions - are bottles integer 
is it possible to left out few bottles ? - yes

numbottles = count 
numbottles/ numexchange division, remainder 

while division + remainder > numexchange 
division + remainder / numexchange  

22 6
3 4


1 1



"""

class solution:
	def max_drinking_bottles(self, numBottles: int, numExchange: int) ->int:
		count = numBottles
		division = numBottles// numExchange
		remainder = numBottles % numExchange
		count += division

		while (division + remainder) >= numExchange: 
			new_total = division + remainder
			division  = new_total // numExchange
			remainder = new_total % numExchange
			count += division  
		return count 
        
test = solution()

print(test.max_drinking_bottles(22,6))