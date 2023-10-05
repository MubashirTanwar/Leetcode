H = [2,3,4,5,18,17,6]
i = 0 
j = len(H) -1
max_vol = 0
a,b = 0,0
while i < j:
    if min(H[i],H[j])*(j-i)>max_vol:
        a,b = H[i],H[j]
        diff = (j-i)
        max_vol = min(H[i],H[j])*(j-i)
    if i<j:
        i+=1
    else:
        j-=1
print(max_vol)
print(a,b)
print(diff)
