'''

Xortholians are a proud race and have a rich history of rainbow-inspired art. One Xortholian artist from the last century made a particularly beautiful series of paintings using only the colors in the rainbow.

Each of these paintings consists of two rows of paint.

The first row is a series of equally sized squares, each of them being a primary color or blank, i.e. each is one of the following: "red", "yellow", "blue", "blank". No two neighboring spaces in the first row will ever have the same color (including blank).

For example, a first row could be:

red blank blue yellow
The second row is a series of colors whose length is one more than its corresponding first row. Each color, in order, is a combination of the two colors above it. Red and blue, for example, make purple, while red and blank would make more red.

A second row generated from the above colors would be:

red red blue green yellow
Visually, the two would look like:

 r   b y
r r b g y
To be clear, possible colors are "red", "orange", "yellow", "green", "blue", and "purple". Xortholians do not recognize indigo or violet.

Your goal as an aspiring young Xortholian Art and Mathematics dual-major is to determine what some paintings' first row is based on the corresponding second row.

Input definition

Input files will consist of a single line having 75 to 100 color names separated by spaces, representing the second row of a painting. Input color names may be "red", "orange" "yellow", "green", "blue", "purple"or "blank".

No two input colors (including "blank") will ever repeat twice in a row.

Output definition

Your output should be a single line consisting of 74 to 99 color names, separated by spaces. Color names may be "red", "yellow", "blue", or "blank".

Example input

red purple green orange purple purple orange yellow yellow yellow
Example output

red blue yellow red blue red yellow blank yellow
'''

a=raw_input().split()
b=[]
c={'orange':'red', 'orange':'yellow', 'green':'yellow', 'green':'blue', 'purple':'blue', 'purple':'red'}
for i in (range(len(a))):
	if (i==0 or i==(len(a)-1)):
		b.append(a[i])
	else:
		if a[i]==a[i-1]:
			b.append('blank')
		else:
			if a[i]==''
