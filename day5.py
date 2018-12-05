import time
start_time = time.time()

def problem1(b): #11476?
    n = len(b) - 1
    i = 0
    while i < n:
        if abs(b[i] - b[i+1]) == 32:
            n -= 2
            del b[i:i+2]
            i = max(0, i - 1)
        else:
            i += 1
    return n + 1

def problem2(): #5446
    #a(A)-z(Z) == 97(65)-122(90)
    minpoly = []
    for x in range(65, 91):
        minpoly.append(problem1([i for i in blob if i != x and i != x + 32]))
    return min(minpoly)


with open("day5.txt") as f:
    blob = [ord(c) for c in f.readline().strip()]

ans1 = problem1(blob)
print("Problem 1:", ans1)
print("Problem 2:", problem2())
print("Runtime:", (time.time() - start_time))
