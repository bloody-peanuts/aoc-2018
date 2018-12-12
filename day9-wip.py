import time
start = time.time()

def marblegame(players, marbles, part1):
    scores = [0] * players
    curmarble, curplayer = 0, 0
    board = []
    boardlen = 0
    removed = set()
    if not part1:
        marbles *= 100
    # perc = round(marbles / 100)
    for m in range(marbles):
        # if m % perc == 0:
            # print(m / perc, '%')
        if m % 23 == 0 and m != 0:
            scores[curplayer] += m
            curmarble = getcurpos(curmarble, boardlen, removed, -7)
            scores[curplayer] += board[curmarble]
            removed.add(curmarble)
            curmarble = getcurpos(curmarble, boardlen, removed, 1)
        else:
            curmarble = getcurpos(curmarble, boardlen, removed, 2)
            board.insert(curmarble, m)
            boardlen += 1
        curplayer += 1
        if curplayer == players:
            curplayer = 0
    return max(scores)



def part2():
    return True

def ct(s, e):
    return round((e - s) * 1000)

def getcurpos(curmarble, iteration, removed, steps):
    if iteration in [0, 1]:
        return iteration
    counter = 0
    if steps < 0:
        while counter < steps:
            curmarble -= 1
            if curmarble < 0:
                curmarble = iteration
            if curmarble not in removed:
                counter += 1
        return curmarble
    while counter < steps:
        curmarble += 1
        if curmarble > iteration:
            curmarble = 0
        if curmarble not in removed:
            counter += 1
    return curmarble


with open('day9.txt') as f:
    inp = f.readline().split()

print('Part 1:', marblegame(int(inp[0]), int(inp[6]), True)) #393229
mid = time.time()
# print('Part 2:', marblegame(int(inp[0]), int(inp[6]), False))
end = time.time()
print('Runtime(ms) - P1:', ct(start, mid), 'P2:', ct(mid, end), 'Total:', ct(start, end))
