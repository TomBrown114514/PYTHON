#质因子
def IsPrime(n):
    '''
    判断是否为素数
    :param n:
    :return:
    '''
    m = 1
    for i in range(2, n):
        if not n % i:
            m = 0
            break
    return m


k = int(input("请输入2-10000之间的正整数："))
print('这个数字的所有质因子为：')
for j in range(2, k + 1):
    if not k % j and IsPrime(j):
        print(j, end=" ")