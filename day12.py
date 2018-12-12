import time
start = time.time()

def calc(n):
    pad = '............................................'
    offset = len(pad)
    oos = offset
    s = pad + state + pad
    padnext = False
    lens = len(s)
    lastvals = []
    lval = 0
    for g in range(n): #n generations
        if padnext == True:
            padnext = False
            lens += (oos * 2)
            offset += oos
            s = pad + s + pad
        ns = '..'
        l2, l1, center, r1, r2 = '.', '.', '.', '.', '.'
        for i in range(4, lens):
            l2, l1, center, r1, r2 = l1, center, r1, r2, s[i]
            nc = hasplant(l2 + l1 + center + r1 + r2)
            ns += nc
            if nc == '#' and (i < 5 or  i > lens - 5):
                padnext = True
        s = ns + '..'
        ival = 0
        for x in range(lens):
            if s[x] == '#':
                ival +=  (x - offset)
        dval = ival - lval
        if len(lastvals) > 5:
            matched = True
            for v in lastvals[-5:]:
                if v != dval:
                    matched = False
                    break
            if matched == True:
                return ival + (dval * (n - g - 1))
        lastvals.append(dval)
        lval = ival
    return ival

def hasplant(s):
    if s in key:
        return key[s]
    return '.'

def ct(s, e):
    return round((e - s) * 1000)


key = {}
plants = set()

with open('day12.txt') as f:
    state = f.readline().split()[2]
    for l in f.readlines()[1:]:
        l = l.split()
        key[l[0]] = l[2]



print('Part 1:',calc(20))
mid = time.time()
print('Part 2:',calc(50000000000))
end = time.time()
print('Time(ms) - P1:', ct(start, mid), 'P2:', ct(mid, end), 'Total:', ct(start, end))
