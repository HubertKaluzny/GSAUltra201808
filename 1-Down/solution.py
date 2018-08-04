import math

def solution(n, c):
    cycles = []
    for swap in c:
        cycles.append(closeCycle(c, list(swap)))

    sum = 1
    for cycle in cycles:
        sum *= pow(2, len(cycle) - 1)

    return sum % (pow(10, 9) + 7)

def closeCycle(c, curr):
    newCycle = curr.copy()
    for elem in curr:
        for swap in c:
            if swap[0] == elem or swap[1] == elem:
                if elem not in newCycle:
                    newCycle.append(elem)

    if len(newCycle) == len(curr):
        return newCycle

    return close_cycle(c, newCycle)
