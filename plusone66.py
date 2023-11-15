# You are given a large integer represented as an integer digitsay digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting digitsay of digits.

# I  H A V E  N O  I D E A   H O W  T H I S  W O R K S
# E X C E L L E N T  E X A M P L E  O F  B O D G I N G

digits = [1,1,1]

sum = 0
for i in range(0,len(digits)):
    sum += digits[i]*10**(len(digits)-1-i)
sum +=1

count = 0
temp = sum
while temp != 0:
    temp //= 10
    count += 1

newdigits = [0]*count
newdigits[0] = (sum//10**abs(count-1))
rem = (sum//10**abs(count-1)) 

for i in range(1,count) : 
    newdigits[i] = (sum//10**abs(count-i-1)) - rem*10
    rem = (sum//10**abs(count-i-1)) 

print(newdigits)