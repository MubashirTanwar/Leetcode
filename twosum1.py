nums = [2,6,11,15]
target = 9
i,j = 0,1
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print(True)
        else:           
            print(False)
