import csv
from collections import defaultdict

# Create dictionary of file names as key and file data as value (list of dictionaries where each dictionary is line/record
# of the file with keys as column names and values as column value)
# Example file_dict = {file_name1: [{'id': '1', 'col1': 'a', 'col2': 'b'}, {'id': '1', 'col1': 'c', 'col2': 'd'}]
#                      file_name2: [{'id': '2', 'col1': 'p', 'col2': 'q'}, {'id': '2', 'col1': 'r', 'col2': 's'}]
#                      }
file_dict = defaultdict(list)
with open('./input.txt') as f:
    for line in f:
        # Skip the empty lines
        if line != '\n':            
            # Remove new line characters from the line
            line = line.strip()
            # Extract column values from input line and store it into the dictionary with keys as column names
            delimited_line = {'id': line[:3], 'coulmn1': line[3:5], 'coulmn2': line[5:]}
            # add record (dictionary) to the list 
            # The file name is first 3 chars in each line that is line[:3]
            file_dict[line[:3]].append(delimited_line)

for file in file_dict:
    # Write data of each file to respective csv file    
    with open(file + '.csv', 'w', newline='') as csvfile:
        column_names = ['id', 'coulmn1', 'coulmn2']

        # The optional restval parameter specifies the value to be written if the dictionary is missing a key in fieldnames
        # The optional extrasaction parameter indicates what action to take If the dictionary passed to the writerow() method 
        # contains a key not found in fieldnames
        writer = csv.DictWriter(csvfile, fieldnames=column_names, restval='', extrasaction='raise')
        writer.writeheader()

        for item in file_dict[file]:
            writer.writerow(item)
