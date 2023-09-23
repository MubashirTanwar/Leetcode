string = "abcd"
sum=""
# for i in range(len(string)):
#     for j in range(i,len(string)):
#         sum = string[i]+string[j]
#         print(string[i]+string[j])
for i in range(len(string)):
    for j in range(i,len(string)):
        for k in range(j,len(string)):
            print(sum+string[k])
