# You are given an array people where people[i] is the weight of the ith person, 
#and an infinite number of boats where each boat can carry a maximum weight of limit. 
#Each boat carries at most two people at the same time, provided the sum of the weight of those people 
#is at most limit.
# Return the minimum number of boats to carry every given person.
# Example 1:
# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)

# Example 2:

# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
people = [3,2,1,1,3,3,3,3,1,1,1]
limit = 3
def numRescueBoats(self, people, limit):
    boats = 0
    people.sort()
    i = 0
    j = len(people)-1
    while(i<=j):
        if people[j]==limit:
            boats+=1
            j-=1
        elif people[j]+people[i]<=limit:
            boats+=1
            j-=1
            i+=1
        else:
            boats+=1
            j-=1
    return boats



# for i in range (len(A)):
#     if A[i] == limit:
#         boats = boats + 1
#     else:
#         while i<len(A)-1:
#             if A[i]+A[i+1]<=limit:
#                 boats=boats+1
#             else:
#                 boats=boats+1
#             break
#         if i== len(A)-1:
#             boats=boats+1