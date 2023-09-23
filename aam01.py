def max_customers(numOfCustomers, customerChoices, numN, numM):
    favorite_plants = [0] * (numN * numM + 1)
    
    for line in customerChoices:
        num_choices = line[0]
        choices = line[1:]
        
        for choice in choices:
            if favorite_plants[choice] == 0:
                favorite_plants[choice] = 1
                break
    
    return sum(favorite_plants)

# Read input
numOfCustomers = int(input())
customerChoices = []
for _ in range(numOfCustomers):
    line = list(map(int, input().split()))
    customerChoices.append(line)

numN = int(input())
numM = int(input())

# Calculate and print the maximum number of customers served
result = max_customers(numOfCustomers, customerChoices, numN, numM)
print(result - 1)  # Subtract 1 to exclude the unused plant 0
