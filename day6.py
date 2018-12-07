import time
start_time = time.time()

def problem1():
    global maxX, minX, maxY, minY, coords
    disq = set()
    tots = [0] * len(coords)
    for x in range(minX, maxX + 1):
        for y in range(minY, maxY + 1):
            cc = -1
            cd = 100
            for i, c in enumerate(coords):
                d = abs(x - c[0]) + abs(y - c[1])
                if d == cd:
                    cc = -1
                elif d < cd:
                    cc = i
                    cd = d
            if cc == -1 or x == maxX or x == minX or y == maxY or y == minY:
                disq.add(cc)
                continue
            tots[cc] += 1
    for d in disq:
        tots[d] = 0
    return max(tots)

def problem2():
    global maxX, minX, maxY, minY, coords
    totalvalid = 0
    for ix in range(minX, maxX + 1):
        for iy in range(minY, maxY + 1):
            if sum([abs(ix - x) + abs(iy - y) for x, y in coords]) < 10000:
                totalvalid += 1
    return totalvalid


def parseImp(c):
    global maxX, minX, maxY, minY
    c = c.split()
    x = int(c[0][:-1])
    y = int(c[1])
    maxX = max(maxX, x)
    maxY = max(maxY, y)
    minX = min(minX, x)
    minY = min(minY, y)
    return [x, y]

minX, minY, maxX, maxY = 1000, 1000, 0, 0

with open('day6.txt') as f:
    coords = [parseImp(c) for c in f.readlines()]

def clock(start, end):
    return round((end - start) * 1000)

print('Problem 1:', problem1()) #3223
mid_time = time.time()
print('Problem 2:', problem2()) #40495
# print(grid)
end_time = time.time()
print("Time - Part 1:", clock(start_time, mid_time), "Part 2: ",
    clock(mid_time, end_time), "Total:", clock(start_time, end_time))
