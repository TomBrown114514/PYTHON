def fbnq(n: int) -> int :
    match n:
        case 1|2:
            return 1
        case _:
            return fbnq(n-2)+fbnq(n-1)

try:
    n = int(input("请输入一个正整数:"))
    assert n > 0, "请输入一个正整数!"
    print(f'第{n}项是{fbnq(n)}')
except AssertionError as ae:
    print(ae)