import os
list_of_filenames = os.listdir("./test")

# test directory has test_1.txt, test_2.txt files

for file in list_of_filenames:

    os.rename("./test/" + file, ("./test/" + file).replace('~', '_'))