'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains
 the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:
Input: height = [1,1]
Output: 1
'''
H = [1,1]
max_vol = 0
for i in range(len(H)):
    for j in range(i+1,len(H)):
        if min(H[i],H[j])*(j-i)>max_vol:
            max_vol = min(H[i],H[j])*(j-i)
        # L U N D     J A I S A     B R U T E F O R C E
print(max_vol)



