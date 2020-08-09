

class Solution:
    def makeGood(self, s: str) -> str:
        
        # "abBAcC"
        
        arr_str = list(s)
        
        is_good = False
        curr_str = ''
        
        if len(arr_str) <= 1:
            return s
        
        while not is_good:
            
            for i in range(len(arr_str) - 1):
                if arr_str[i].upper() == arr_str[i+1].upper() and arr_str[i] != arr_str[i+1]:
                    arr_str[i] = '0'
                    arr_str[i+1] = '0'

            arr_str[:] = [x for x in arr_str if x != '0']

            if not arr_str or len(arr_str) == 1:
                is_good = True
            for i in range(len(arr_str) -1):
                print("was ")
                print(arr_str)

                is_good = True
                if arr_str[i].upper() == arr_str[i+1].upper() and arr_str[i] != arr_str[i+1]:
                     is_good = False
                     break
            
        return "".join(arr_str)

test = Solution()

print(test.makeGood("qFxXfQo"))