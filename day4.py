import time
start_time = time.time()

def problem1():
    maxsleep = 0
    ans = 0
    for g in inp:
        tot = sum(inp[g])
        if tot > maxsleep:
            maxsleep = tot
            ans = g * inp[g].index(max(inp[g]))
    return ans


def problem2():
    maxtimes = 0
    ans = 0
    for g in inp:
        thismax = max(inp[g])
        if thismax > maxtimes:
            maxtimes = thismax
            ans = g * inp[g].index(thismax)
    return ans

def parseShifts(entries):
    g = {}
    guard = 0
    fell = 0
    for i in entries:
        type = i[-3]
        if type == 'f': #Begins shift
            guard = int(i.split(' ', 4)[3][1:])
            continue
        if type == 'e': #falls asleep
            fell = int(i.split(':', 2)[1][:2])
            continue
        if type == 'u': #wakes up
            if guard not in g:
                g[guard] = [0] * 60
            woke = int(i.split(':', 2)[1][:2])
            for x in range(fell, woke):
                g[guard][x] += 1
    return g

with open("day4.txt") as f:
    inp = parseShifts(sorted(f.readlines()))

print("Problem 1:", problem1())
print("Problem 2:", problem2())
print("Runtime:", (time.time() - start_time))
