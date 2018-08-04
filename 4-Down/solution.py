import math

def solution(l, r):
    fibPrimes = [2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437, 2971215073, 99194853094755497, 1066340417491710595814572169, 19134702400093278081449423917]
    notFibPrimes = getPrimes(math.ceil(math.sqrt(r)))

    for p in fibPrimes:
        if p in notFibPrimes:
            notFibPrimes.remove(p)
        else:
            break

    num = 0

    for i in range(l, r + 1):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
            continue
        for p in notFibPrimes:
            if p > i:
                break
            if i % p == 0:
                num += 1
                break

    return num

def getPrimes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes
