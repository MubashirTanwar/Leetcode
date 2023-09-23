class Solution:
    def containsDuplicate( nums) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                print(True) 
    A = [1,2,3,1]
    containsDuplicate(A)