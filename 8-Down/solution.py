import bisect
from heapq import heappush, heappop

def solution(n, m, r, c, k):
    rowDiff = []
    colDiff = []
    k -= 1
    for i in range(1, len(r)):
        diff = r[i] - r[i - 1]
        bisect.insort(rowDiff, diff)

    for i in range(1, len(c)):
        diff = c[i] - c[i - 1]
        bisect.insort(colDiff, diff)

    rooms = len(rowDiff) * len(colDiff)
    
    if(k > int(rooms / 2)):
      rowDiff = list(reversed(rowDiff))
      colDiff = list(reversed(colDiff))
      k = rooms - k

    queue = [(rowDiff[0] * colDiff[0], (0, 0))]
    elements = 0

    while elements < k:
      (_, elem) = heappop(queue)
      elements += 1
      if elem[0] == 0:
        a = (0, elem[1] + 1)
        if a[1] < len(colDiff):
          heappush(queue, (rowDiff[a[0]] * colDiff[a[1]], a))
        b = (1, elem[1])
        if b[1] < len(colDiff):
          heappush(queue, (rowDiff[b[0]] * colDiff[b[1]], b))
      else:
        a = (elem[0] + 1, elem[1])
        if a[0] < len(rowDiff) and a[1] < len(colDiff):
          heappush(queue, (rowDiff[a[0]] * colDiff[a[1]], a))

    (size, _) = heappop(queue)
    return size
