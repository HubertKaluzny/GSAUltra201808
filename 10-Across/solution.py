def solution(t_n, t_a, t_b, t_x, t_y):
    W = 0
    for i in range(0, len(t_n)):
        W += doesAliceWin(t_n[i], t_a[i], t_b[i], t_x[i], t_y[i])
    return (W + 123)

def doesAliceWin(n, a, b, x, y):
    aliceTurn = True

    while(n > 0):
        if n >= 1 and n <= 3:
            n = 0
            aliceTurn = not aliceTurn
            break

        divA = x
        divB = y
        if aliceTurn:
            divA = a
            divB = b

        most = -1
        for i in range(3, n + 1):
            if i % divA != 0 and i % divB != 0:
                most = i

        if most == -1:
            if aliceTurn:
                return 0
            return 1

        n -= most
        aliceTurn = not aliceTurn

    if(aliceTurn):
        return 0
    return 1 
