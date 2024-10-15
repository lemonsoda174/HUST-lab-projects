    n = int(input())
    d = []

    for _ in range(n+1):
        a = list(map(int, input().split()))
        d.append(a)

    def greedytsp(d, n):
        cur = 1
        s = [cur]
        c = set()
        for i in range(1, n+1):
            if i != cur:
                c.add(i)  
        f = 0

        while len(c) > 0:
            x = select(c, cur)
            f += d[cur-1][x-1]
            s.append(x)
            c.remove(x)
            cur = x
            
        #f += d[cur][1]

        return s

    def select(c, cur):
        minD = 1000000000
        for x in c:
            if d[cur-1][x-1] < minD:
                minD = d[cur-1][x-1]
                selectpoint = x
        return selectpoint
    print(n)
    for item in greedytsp(d, n):
        print(item, end = ' ')
