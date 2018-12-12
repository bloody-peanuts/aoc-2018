import time
start = time.time()

def part1():
    maxpower = -1000
    maxcoord = []
    for x in range(298):
        for y in range(298):
            val = 0
            for thisx in range(x, x + 3):
                for thisy in range(y, y + 3):
                    val += grid[thisx][thisy]
            if val > maxpower:
                maxpower = val
                maxcoord = [x, y]
    return maxcoord

def part2():
    maxpower = 0
    maxcoord = []
    for x in range(300):
        for y in range(300):
            val = 0
            for s in range(1, 300 - max(x, y)):
                for thisx in range(x, x + s):
                    val += grid[thisx][y + s]
                for thisy in range(y + 1, y + s + 1):
                    val += grid[x + s][thisy]
                if val > maxpower:
                    maxpower = val
                    maxcoord = [x, y, s + 1]
    return maxcoord

def calcvalue(x, y):
    rackid = x + 10
    ret = (rackid * y) + serial
    ret *= rackid
    return ((ret // 100) % 10) - 5

def ct(s, e):
    return round((e - s) * 1000)

with open('day11.txt') as f:
    serial = int(f.readline())

grid = [[[] for i in range(300)] for i in range(300)]

for x in range(300):
    for y in range(300):
        grid[x][y] = calcvalue(x, y)


with open('day9.txt') as f:
    inp = f.readline().split()

for x in range(2,2):
    print(x)
print('Part 1:', part1())
mid = time.time()
print('Part 2:', part2())
end = time.time()
print('Runtime(ms) - P1:', ct(start, mid), 'P2:', ct(mid, end), 'Total:', ct(start, end))
