def zdgys(m, n):
    """
    求最大公约数和最小公倍数。
    :param m: 第一个整数
    :param n: 第二个整数
    :return: 最小公倍数和最大公约数
    """
    c = m if m < n else n
    for i in range(1, c + 1):
        if m % i == 0 and n % i == 0:
            t = i
    a = m * n / t
    return f"{m}和{n}的最大公约数是{t}，最小公倍数是{a}"


def zzxcf(ma, mi):
    """
    使用辗转相除法求最大公约数和最小公倍数
    :param ma: 第一个整数
    :param mi: 第二个整数
    :return: 最大公约数和最小公倍数
    """
    a, b = ma, mi
    while 1:
        t = mi
        mi = ma % mi
        ma = t
        if mi == 0:
            return f"{a}和{b}的最大公约数是{t}，最小公倍数是{a * b / t}"


if __name__ == "__main__":
    m = int(input("请输入第一个数："))
    n = int(input("请输入第二个数："))

    print(f"使用优化方法解出的结果是：{zdgys(m, n)}")
    print(f"使用辗转相除法解出的结果是：{zzxcf(m, n)}")
