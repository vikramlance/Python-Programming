'''
Given a set of lines each containing multiple random strings, your task for each line is to find the characters that are common to all of its strings. In other words, you should output one string for each line that contains all of the distinct characters that the given strings on that line have in common.

Characters include [A-Z, a-z, 0-9]. Characters with different cases (e.g. 'a' vs 'A') count as distinct characters.

The order of characters in the output string should appear as follows:

In order of numbers 0-9.
In order of uppercase characters A-Z.
In order of lowercase characters a-z.
Input definition

Input files for this problem will contain an arbitrary number of lines.

The first line will contain an integer, m, denoting the number of tests in the input file.

Each subsequent line will contain multiple space-separated strings.

Output definition

Your output should contain m lines, one corresponding to each test case given in the input.

Each line should have one string (which can be empty/a blank line) containing all of the distinct characters that the input strings have in common, listed in the order described above.

Example input

2
9x34209asAb32sD840D9258 02934x2DoebAaab90CDEe348290
aabcwdefghkij ksdfopweiraa wieourslakaaier asjoirwekjaa
Example output

023489ADabx
aeikw

'''



a= int(raw_input())

for i in range(a):
    b= raw_input().split()
    for k in range(len(b)):
        if (k ==0):
            m=set(b[k])
        else:
            m=(m & set(b[k]))
    print ''.join(map(str,sorted(m)))
