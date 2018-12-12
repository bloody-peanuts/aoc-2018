import time
start = time.time()

def solve():
    for second in range(10607):
        minx, miny, maxx, maxy = 100000, 100000, 0, 0
        outp = {}
        for x in range(len(points)):
            p = points[x]
            minx, miny, maxx, maxy = min(minx, p[0][0]), min(miny, p[0][1]), max(maxx, p[0][0]), max(maxy, p[0][1])
            if p[0][1] not in outp:
                outp[p[0][1]] = set()
            outp[p[0][1]].add(p[0][0])
            points[x][0][0] += p[1][0]
            points[x][0][1] += p[1][1]
        if maxx - minx < 75:
            print('')
            print('')
            print('')
            print('')
            print('Second #', second)
            for y in range(miny, maxy + 1):
                yout = ''
                for x in range(minx, maxx + 1):
                    if y in outp and x in outp[y]:
                        yout += '#'
                    else:
                        yout += '.'
                print(yout)

def parsein(s):
    s = s.split()
    return [[int(s[0]), int(s[1])], [int(s[2]), int(s[3])]]

with open('day10.txt') as f:
    points = [parsein(x) for x in f.readlines()]

solve() #BXJXJAEX at second 10605
print('Runtime(ms):', round((time.time() - start) * 1000))
