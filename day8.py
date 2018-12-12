import time
import sys
start = time.time()
sys.setrecursionlimit(10000)
totalmeta = 0

def part1():
    global totalmeta
    return totalmeta

def part2(n):
    nodex = len(n['nodes'])
    if nodex == 0:
        return sum(n['meta'])
    val = 0
    for x in n['meta']:
        if x == 0 or x > nodex:
            continue
        val += part2(n['nodes'][x - 1])
    return val


def gettree(s):
    global totalmeta
    nodex = s[0]
    metax = s[1]
    s = s[2:]
    ns = []
    for x in range(nodex):
        child, s = gettree(s)
        ns.append(child)
    meta = s[:metax]
    totalmeta += sum(meta)
    return [{'nodes': ns, 'meta': meta}, s[metax:]]

def ct(s, e):
    return round((e - s) * 1000)

with open('day8.txt') as f:
    inp = [int(x) for x in f.readline().split()]

tree, leftovers = gettree(inp)
print('Part 1:', part1())
mid = time.time()
print('Part 2:', part2(tree))
end = time.time()
print('Runtime(ms) - P1:', ct(start, mid), 'P2:', ct(mid, end), 'Total:', ct(start, end))
