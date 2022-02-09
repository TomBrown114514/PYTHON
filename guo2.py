for i in range(10000,100000):
    s = 0
    for j in str(i):
        s = s + int(j)**5
        if s==i:
            print(i)