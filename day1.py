import time
start_time = time.time()

def problem1():
    total = 0
    for x in input1:
        total += x
    return total

def problem2():
    total = 0
    s = set()
    while True:
        for x in input1:
            total += x
            if total in s:
                return total
            s.add(total)

with open("day1.txt") as f:
    input1 = [int(x.strip()) for x in f.readlines()]

print('Problem 1: ', problem1())
print('Problem 2: ', problem2())
print("Runtime:", (time.time() - start_time))
