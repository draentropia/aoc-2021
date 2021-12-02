# read input
f = open('day2_input.txt', 'r')
inps = f.readlines()

directions = {
    "forward" : 0,
    "up" : 0,
    "down" : 0
}

for i in inps:
    directions[i.split()[0]] += int(i.split()[1])

print("forward", directions["forward"])
print("up", directions["up"])
print("down", directions["down"])

solution = (directions["down"]-directions["up"])*directions["forward"]
print(solution)

aim = 0
depth = 0
fw = 0
up = 0
down = 0
for i in inps:
    if i.split()[0] == "forward":
        fw += int(i.split()[1])
        if aim != 0:
            depth += aim*int(i.split()[1])
    if i.split()[0] == "up":
        aim -= int(i.split()[1])
    if i.split()[0] == "down":
        aim += int(i.split()[1])

solution_2 = depth * fw
print(solution_2)