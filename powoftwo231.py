import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<1:
            return False
        else:
            if abs(math.log2(n)).is_integer():
                return True