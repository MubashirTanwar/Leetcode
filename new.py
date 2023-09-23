arr = [2,3,5,4,1,8,12,9]
newArr=[]
maxNum=0
count = 0
k =0
index=0
for i in range(len(arr)):
    if arr[i]>k:
        k = arr[i]
        index = i
while len(arr)>index:
    arr.pop()
print(arr)
k =0
index=0
for i in range(len(arr)):
    if arr[i]>k:
        k = arr[i]
        index = i
while len(arr)>index:
    arr.pop()
print(arr)
k =0
index=0
for i in range(len(arr)):
    if arr[i]>k:
        k = arr[i]
        index = i
while len(arr)>index:
    arr.pop()
print(arr)

