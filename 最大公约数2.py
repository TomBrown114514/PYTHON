# 输入两个正整数
m = int(input('请输入第一个正整数：'))
n = int(input('请输入第二个正整数：'))
if m <= 0 or n <= 0:  # 如果有其中一个不是正整数，输出提示。
    print('这两个数都必须是正整数！')
else:
    c = m if m < n else n  # 找出两个数的最小的一个
    for i in range(1, c + 1):
        if m % i == 0 and n % i == 0:  # 找出两个数共有的约数
            j = i
    t = m * n / j
    print(f'\n{m}和{n}的最大公约数是{j}，最小公倍数是{t}')
