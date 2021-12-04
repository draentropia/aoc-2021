import numpy as np

# read input
f = open('day3_input.txt', 'r')
inps = f.readlines()

# part 1
sum_digits = []
count_inputs = 0
for i in inps:
    digits = [int(x) for x in str(int("9"+i))] # add a random number to avoid removing the initial 0
    # Delete the added value
    digits.pop(0)
    for i in range(len(digits)):
        if len(sum_digits) != len(digits):
            sum_digits.append(digits[i])
        else:
            sum_digits[i] += digits[i]
    count_inputs += 1
    # Check if each value of sum_digits is higher than the half of total values
gamma = "" # most common bit    
epsilon = "" # less common bit
for sd in sum_digits:
    if sd < (count_inputs/2):
        gamma += "0"
        epsilon += "1"
    if sd > (count_inputs/2):
        gamma += "1"
        epsilon += "0"
    if sd == (count_inputs/2): #cannot be but at least test
        break

print("solution", int(gamma, 2) * int(epsilon, 2))

# part 2: for the future
