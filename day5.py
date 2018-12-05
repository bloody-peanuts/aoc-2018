import time
start_time = time.time()

def problem1(b, r):
    past = [0]
    for i in b:
        if abs(i - past[-1]) == 32:
            past.pop()
        else:
            past.append(i)
    if r:
        global blob
        blob = past[1:]
    return len(past) - 1

def problem2(): #5446
    #a(A)-z(Z) == 97(65)-122(90)
    minpoly = []
    for x in range(65, 91):
        minpoly.append(problem1([i for i in blob if i != x and i != x + 32], False))
    return min(minpoly)


with open("day5.txt") as f:
    blob = [ord(c) for c in f.readline().strip()]

ans1 = problem1(blob, True)
print("Problem 1:", ans1)
mid_time = time.time()
print("Problem 2:", problem2())
end_time = time.time()
print("Problem 1 time:", (mid_time - start_time))
print("Problem 2 time", (end_time - mid_time))
print("Runtime:", (end_time - start_time))
