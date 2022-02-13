def zxgbs(a, b):
    """
    求最大公约数和最小公倍数。若a,b都不是正整数则抛出异常。
    :param a: 第一个正整数
    :param b: 第二个正整数
    :return: 最大公约数和最小公倍数
    """
    if a <= 0 or b <= 0:
        raise Exception("两个数必须均为正整数！")
    c = b if a >= b else a
    for i in range(1, c + 1):
        if a % i == 0 and b % i == 0:
            j = i
    return j, a * b / j


try:
    m = int(input("请输入第一个正整数："))
    n = int(input("请输入第二个正整数："))
    o = zxgbs(m, n)
    print(f"\n使用优化方法解出的结果是：\n{m}和{n}的最大公约数是{o[0]}，最小公倍数是{o[1]}")
except Exception as Err:
    print(f"\n出错啦！{Err}！")
