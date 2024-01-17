class Solution:
    def isPalindrome(self, x: int) -> bool:
        list1=[]
        import math
        y = [a for a in str(x)]
        for i in range(0,math.floor(len(y)/2)+1):
            if y[i]!=y[-i-1]:
              list1.append(1)
            else:
              list1.append(0)
        if 1 in list1:
          return False
        return True