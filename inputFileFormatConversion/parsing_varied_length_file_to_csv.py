from collections import defaultdict

# Create dictionary of file names as key and file data as value (list of values)
# Example file_dict = {file_name1: ['line1', 'line2'], file_name2: ['line3', 'line4']}
file_dict = defaultdict(list)
with open('./input.txt') as f:
    for line in f:
        # Skip the empty lines
        if line != '\n':
            # The file name is first 3 chars in each line that is line[:3]
            # Add line to respective file name 
            file_dict[line[:3]].append(line)

for file in file_dict:
    # Write data of each file to respective csv file
    with open(file + '.csv', 'w') as f:
        for item in file_dict[file]:
            f.write("%s" % item)
