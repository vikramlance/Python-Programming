import re 

# re.sub(pattern, repl, string, count=0, flags=0)

# re.findall(pattern, string, flags=0)

input_str = '<tag1>abcd</tag1><tag2>abcd</tag2><tag3>abcd</tag3><tag4>abcd</tag4><tag5>abcd</tag5><tag1>abcd</tag1><tag2>abcd</tag2><tag3>abcd</tag3><tag4>abcd</tag4><tag5>abcd</tag5>'

result = re.findall('(?<=tag2).*?(?=/tag4)', input_str)

print(result)

"""
 # Python 3 program to find number of
# different sub strings
 
# function to return number of different
# sub-strings
def numberOfDifferentSubstrings(s, a, b):
 
    # initially our answer is zero.
    ans = []
 
    # find the length of given strings
    ls = len(s)
    la = len(a)
    lb = len(b)
 
    # currently make array and initially
    # put zero.
    x = [0] * ls
    y = [0] * ls
 
    # find occurrence of "a" and "b" in string "s"
    for i in range(ls):
         
        if (s[i: la + i] == a):
            x[i] = 1
        if (s[i: lb + i] == b):
            y[i] = 1
 
    # We use a hash to make sure that same
    # substring is not counted twice.
    hash = []
 
    # go through all the positions to find
    # occurrence of "a" first.
    curr_substr = ""
    for i in range(ls):
     
        # if we found occurrence of "a".
        if (x[i]):
         
            # then go through all the positions
            # to find occurrence of "b".
            for j in range( i, ls):
             
                # if we do found "b" at index
                # j then add it to already
                # existed substring.
                if (not y[j]):
                    curr_substr += s[j]
 
                # if we found occurrence of "b".
                if (y[j]):
                 
                    # now add string "b" to
                    # already existed substring.
                 
                    curr_substr += s[j: lb + j]
                     
                    # If current substring is not
                    # included already.
                    if curr_substr not in hash:
                        ans.append(curr_substr)
 
                    # put any non negative integer
                    # to make this string as already
                    # existed.
                    hash.append(curr_substr)

 
            # make substring null.
            curr_substr = ""
    print(hash)
    # return answer.
    return ans
 
# Driver Code
if __name__ == "__main__":
     
    s = '<tag1>abcd</tag1><tag2>abcd</tag2><tag3>abcd</tag3><tag4>abcd</tag4><tag5>abcd</tag5><tag1>abcd</tag1><tag2>abcd</tag2><tag3>abcd</tag3><tag4>abcd</tag4><tag5>abcd</tag5>'
    # "codecppforfood"
    begin = "<tag3>"
    end = "</tag4>"
    print(numberOfDifferentSubstrings(s, begin, end))
 
"""