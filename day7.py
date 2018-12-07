import copy
import time

start = time.time()

def part1(r):
    r = r.copy()
    ans = ''
    left = sorted(r.keys())
    while len(left) > 0:
        for k in left:
            if r[k] == []:
                del r[k]
                ans += k
                left.remove(k)
                for e in r:
                    if k in r[e]:
                        r[e].remove(k)
                break
    return ans

def part2(r): #ord(x) - 64
    clk = -1 #So we can have the first tick be `0`
    wrks = []
    left = sorted(r.keys())
    while len(left) > 0 or len(wrks) > 0:
        clk += 1
        if len(wrks) > 0:
            wd = []
            for x in range(len(wrks)):
                wrks[x][0] -= 1
                if wrks[x][0] == 0:
                    k = wrks[x][1]
                    del r[k]
                    for e in r:
                        if k in r[e]:
                            r[e].remove(k)
                    wd.append(x)
            for d in wd:
                del wrks[d]
        for k in left:
            if len(wrks) > 4:
                break
            if r[k] == []:
                wrks.append([ord(k) - 4, k])
                left.remove(k)
    return clk


reqs = dict()

with open('day7.txt') as f:
     inp = f.readlines()

for l in inp:
    l = l.split()
    s, r = l[7], l[1]
    if r not in reqs:
        reqs[r] = []
    if s not in reqs:
        reqs[s] = []
    reqs[s].append(r)

def clockMs(s, e):
    return round((e - s) * 1000)


print("Part 1:", part1(copy.deepcopy(reqs))) #BGJCNLQUYIFMOEZTADKSPVXRHW
mid = time.time()
print("Part 2:", part2(reqs)) #1017
end = time.time()
print("Time(ms): P1:", clockMs(start, mid), "P2:", clockMs(mid, end), "Tot:", clockMs(start, end))
