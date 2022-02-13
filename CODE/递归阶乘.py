def jc(n):
    return 1 if n==1 else n*jc(n-1)

Sum = 0
N = int(input())
for i in range(1,N+1):
    Sum = Sum + jc(i)
print(Sum)
