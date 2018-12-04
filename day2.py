import time
start_time = time.time()

def problem1():
    twos = 0
    threes = 0
    for s in input1:
        if containsExact(s, 2):
            twos += 1
        if containsExact(s, 3):
            threes += 1
    return twos * threes


def problem2():
    while len(input1) > 2:
        s = input1.pop()
        for i in input1:
            c = 0
            for x in range(len(s)):
                if s[x] != i[x]:
                    c += 1
                    if c > 1:
                        continue
            if c == 1: #success!
                ret = ''
                for x in range(len(s)):
                    if s[x] == i[x]:
                        ret += s[x]
                return ret
    return "No match found"


def containsExact(s, i):
    for c in s:
        if s.count(c) == i:
            return True
    return False

with open("day2.txt") as f:
    input1 = [x.strip() for x in f.readlines()]

print('Problem 1: ', problem1())
print('Problem 2: ', problem2())
print('Runtime: %s seconds' % (time.time() - start_time))
