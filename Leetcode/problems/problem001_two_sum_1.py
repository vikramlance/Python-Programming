class solution:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def get_two_sum(self):
        arr = self.arr
        target = self.target

        temp_dict = {}

        for i in range(len(arr)):
            second_element = target - arr[i]
            if second_element in temp_dict:
                return [temp_dict[second_element], i]

            temp_dict[arr[i]] = i


arr = [1, 4, 8, 9, 2]
target = 11
test = solution(arr, target)

print(test.get_two_sum())
