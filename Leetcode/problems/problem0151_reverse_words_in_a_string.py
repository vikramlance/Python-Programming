class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        arr_reverse = arr[::-1]
        
        return " ".join(x for x in arr_reverse)
        