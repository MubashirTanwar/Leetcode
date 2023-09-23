# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#     [1]
#    [1,1]
#   [1,2,1]
#  [1,3,3,1]
# [1,4,6,4,1]
numRows = 6

bigArr = [ [1]*x for x in range(1,numRows+1)]
for row in range(2, numRows):
    for col in range(1, len(bigArr[row])-1 ):
        bigArr[row][col] = bigArr[row-1][col-1] + bigArr[row-1][col]
print(bigArr)