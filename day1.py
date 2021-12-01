f = open('day1_input.txt', 'r')
inps = f.readlines()
incr = 0
for i in range(0, len(inps)-1):
    if int(inps[i]) < int(inps[i+1]):
        incr += 1
print("part 1", incr) #1462

incr_3 = 0

for i in range(0, len(inps)-3):
    if (int(inps[i])+int(inps[i+1])+int(inps[i+2])) < (int(inps[i+1])+int(inps[i+2])+int(inps[i+3])):
        incr_3 += 1
print("part 2", incr_3)