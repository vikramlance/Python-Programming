import re 

# re.findall(pattern, string, flags=0)

with open('input_string.txt') as f:
    for line in f:
        input_str = line

result = re.findall('(?<=tag2).*?(?=/tag4)', input_str)

print(result)
