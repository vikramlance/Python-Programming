"""
sort following list of versions
versions = ['1.3.0.9', '0.2.0', '3.1.2', '0.1.6', '5.0.0', '3.3.3.3', '3.3.3.3.3', '3.10', '0.2.0']


split based on . 
Convert list of strings to list of numbers
Sort list of list and then convert back to list of strings 
arrange numbers based on first digit, then second digit and so on .. 

"""

class solution:
    def sort_versions(self, versions):
        # for i in versions:
        #     print((i.split('.')))

        versions.sort(key=lambda s: list(map(int, s.split('.'))))

        # versions_list.sort(key=lambda s: [int(u) for u in s.split('.')])

        return versions


test = solution()
versions = ['1.3.0.9', '0.2.0', '3.1.2', '0.1.6', '5.0.0', '3.3.3.3', '3.3.3.3.3', '3.10', '0.2.0']

print(test.sort_versions(versions))
