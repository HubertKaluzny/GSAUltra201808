import copy

def solution(n, x, r):
    return calc(n, x, r) * 10000

def calc(n, x_t, r_t):
    x = list(x_t)
    r = list(r_t)

    if n == 0:
        return 0

    explosionMatrix = [[]] * n

    for i in range(0, n):
        explosionMatrix[i] = findSecondary(n, x, r, [i])

    best = 0
    for i in range(0, n):
        if len(explosionMatrix[i]) > len(explosionMatrix[best]):
            best = i

    newN = n
    newX = x.copy()
    newR = r.copy()

    for exp in explosionMatrix[best]:
        newN -= 1
        rElem = r[exp]
        xElem = x[exp]
        newR.remove(rElem)
        newX.remove(xElem)

    return 1 + calc(newN, newX, newR)

def findSecondary(n, x, r, explosions):
    secondaryExplosions = copy.deepcopy(explosions)

    for i in explosions:
        dist = x[i]
        power = r[i]
        for j in range(0, n):
            if j == i:
                continue
            if j in secondaryExplosions:
                continue
            if(abs(dist - x[j]) <= power):
                secondaryExplosions.append(j)
    if len(secondaryExplosions) == len(explosions):
        return secondaryExplosions

    return findSecondary(n, x, r, secondaryExplosions)
