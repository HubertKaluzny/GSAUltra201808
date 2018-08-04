from collections import deque

def solution(n,m):
    startPos = findInMaze(m, 'S')
    goals = ['R', 'G', 'B']
    totalLength = 0
    pos = startPos
    while goals:
        (newPos, pathLen) = findShortestPathTo(m, pos, goals)
        goals.remove(m[newPos[0]][newPos[1]])
        totalLength += pathLen
        pos = newPos

    (_, pathLen) = findShortestPathTo(m, pos, ['C'])
    totalLength += pathLen

    return pathLen * 1000

def findInMaze(m, char):
    for x in range(0, len(m)):
        for y in range(0, len(m)):
            if m[x][y] == char:
                return (x, y)

    return (-1, -1)

def findShortestPathTo(m, start, goals):
    queue = deque([(0, start)])
    visited =  set()

    while queue:
        (pathLength, curr) = queue.popleft()

        if curr[0] >= len(m) or curr[1] >= len(m):
            continue
        if m[curr[0]][curr[1]] in goals:
            return (curr, pathLength)
        if m[curr[0]][curr[1]] == 'W':
            continue
        if curr in visited:
            continue
        visited.add(curr)
        queue.append((pathLength + 1, (curr[0], curr[1] + 1)))
        queue.append((pathLength + 1, (curr[0], curr[1] - 1)))
        queue.append((pathLength + 1, (curr[0] + 1, curr[1])))
        queue.append((pathLength + 1, (curr[0] - 1, curr[1])))

    return None
