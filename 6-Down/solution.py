import copy

def solution(t):
    sum = 0
    for i in range(0, len(t)):
        (n, m, k) = t[i]
        sum += (pow(2, i) * testProb(n, m, k))

    return sum % (pow(10, 9) + 7)

def testProb(n, m, k):
    inDeg = []
    openNodes = []

    for i in range(0, n):
        inDeg.append(0)

    for (u, v) in m:
        inDeg[v - 1] += 1

    for i in range(0, n):
        if inDeg[i] == 0:
            openNodes.append(i + 1)

    return topoSortFor(openNodes, inDeg, m, k)

def topoSortFor(openNodes, inDeg, m, k):

    if equalNodes(openNodes, k):
        return 1

    if len(openNodes) == 0:
        return 0

    for node in openNodes:
        newInDeg = copy.deepcopy(inDeg)
        newOpenNodes = copy.deepcopy(openNodes)
        newOpenNodes.remove(node)

        for (u, v) in m:
            if u == node:
                newInDeg[v - 1] -= 1
                if newInDeg[v - 1] == 0:
                    newOpenNodes.append(v)
                    if equalNodes(newOpenNodes, k):
                        return 1

        if equalNodes(newOpenNodes, k):
            return 1

        if topoSortFor(newOpenNodes, newInDeg, m, k) == 1:
            return 1

    return 0

def equalNodes(A, B):
    for a in A:
        if a not in B:
            return False

    for b in B:
        if b not in A:
            return False

    return True
