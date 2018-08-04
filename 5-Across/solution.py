def solution(a, b):
    copies = 0
    builtOfA = 0

    while builtOfA < len(a):
      bLeftOvers = b
      built = 0
      nextChar = a[builtOfA]
      bLeftOvers = bLeftOvers.split(nextChar, 1)

      while len(bLeftOvers) > 1:
        bLeftOvers = bLeftOvers[1]
        builtOfA += 1
        built += 1
        if builtOfA >= len(a):
          break
        nextChar = a[builtOfA]
        bLeftOvers = bLeftOvers.split(nextChar, 1)
      copies += 1

    return copies
