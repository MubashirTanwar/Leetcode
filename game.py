# ACM SEMICODE ROUND 2 QUESTION 1
arr = [3,1,8,9,7,6,0,5,9,10]
count = 0
while len(arr)!=0:
    k =0
    index=0
    count+=1
    for i in range(len(arr)):
        if arr[i]>k:
            k = arr[i]
            index = i
    while len(arr)>index:
        arr.pop()
if count%2 == 0:
    print("ANDY")
else:
    print("BOB")