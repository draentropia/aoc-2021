import numpy as np

# read input
f = open('day3_input.txt', 'r')
inps = f.readlines()

# convert input to matrix
matrix = []
for i in inps:
    digits = [int(x) for x in str(int(i))]
    matrix.append(digits)

M = np.array(matrix)

r = [row[0] for row in M]

print(r)