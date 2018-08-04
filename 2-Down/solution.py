def solution(s):
    colourSet = set(s)
    C = 0
    current = len(colourSet)

    while len(s) > 0 and not len(s) < 2 * len(colourSet):
        if not isSuperColourful(s[0:current + 1], colourSet):
            C += 1
            s = s[current - 1:]
            current = len(colourSet)
        else:
            current += 1

    return 10000 + C;

def isSuperColourful(s, colourSet):
    subColourSet = set(s)
    if len(s) < len(colourSet):
        return False

    if len(subColourSet ^ colourSet) > 0:
        return False

    colourMap = {}
    for c in colourSet:
        colourMap[c] = 0

    for i in range(0, len(s)):
        colourMap[s[i]] += 1

    for a in colourSet:
        for b in colourSet:
            if colourMap[a] == colourMap[b]:
                return False

    return True
