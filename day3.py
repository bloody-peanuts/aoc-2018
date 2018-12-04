import time
start_time = time.time()

once = set()
multi = set()

def calc():
    for i in inp:
        for x in range(i[0][0], i[0][0] + i[1][0]):
            for y in range(i[0][1], i[0][1] + i[1][1]):
                coords = x * 1024 + y
                if coords in once:
                    multi.add(coords)
                else:
                    once.add(coords)
    return len(multi)

def calc2():
    for i in inp:
        olap = False
        for x in range(i[0][0], i[0][0] + i[1][0]):
            for y in range(i[0][1], i[0][1] + i[1][1]):
                coords = x * 1024 + y
                if coords in multi:
                    olap = True
                if olap:
                    break
            if olap:
                break
        if olap == False:
            return i[2]
    return False


def parseInput(i):
    i = i.split()
    coords = i[2].split(',')
    dims = i[3].split('x')
    x = int(coords[0])
    y = int(coords[1][:-1])
    w = int(dims[0])
    h = int(dims[1])
    return ([[x, y], [w, h], int(i[0][1:])])

with open('day3.txt') as f:
    inp = [parseInput(x) for x in f.readlines()]

print("Problem 1:", calc())
print("Problem 2:", calc2())
print("Runtime:", time.time() - start_time)
