# You are given two positive integer arrays spells and potions, of length n and m respectively,
#  where spells[i] represents the strength of the ith spell and potions[j] represents the strength 
# of the jth potion.

# You are also given an integer success. A spell and potion pair is considered successful if the
#  product of their strengths is at least success.

# Return an integer array pairs of length n where pairs[i] is the number of potions that will 
# form a successful pair with the ith spell.
spells = [3,1,2]
potions = [8,5,8]
success = 16
potions.sort()
pairs=[]
for i in range(len(spells)):
    count =0
    res = [x * spells[i] for x in potions]
    l = 0
    r = len(res)
    while l<r:
        mid = (l + (r-l))/2
        if mid < success:
             l = mid + 1
        else:
            r = mid
print(pairs)