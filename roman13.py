# PYTHON 3 Sol in onmline compiler
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10,'V': 5,'I': 1}
        i,j = 0,0
        for i in range(len(s)-1,-1,-1):
            temp = roman[s[i]]
            if i > temp:
                j -= temp
            else:
                j += temp
            i = temp
        return j