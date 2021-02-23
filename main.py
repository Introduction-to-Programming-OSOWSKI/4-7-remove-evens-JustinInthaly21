def removeEvens(k):
    g = k
    h = 0
    for i in range(0, len(k)):
        if g[i - h] % 2 == 0 and g[i - h] != 0:
            g.pop(i - h)
            h = h + 1

    return g
            
