def is_leap(year):
    leap = False
    if (year%400==0):
        leap=True
    else:
        if (year%100 ==0 ):
            leap=False
        else:
			if (year%4 ==0):
				leap=True
			else:
				leap=False
     
    # Write your logic here
    
    return leap

year = int(raw_input())
print is_leap(year)
