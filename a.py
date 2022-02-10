#使用版本：Python 3.11.0a5
def fbid(n: int) -> int :
    match n:
        case 1|2:
            return 1
        case _:
            return fbid(n-2)+fbid(n-1)

try:
    n = int(input("请输入一个正整数:"))
    assert n > 0, "请输入一个正整数!"
    print(f'第{n}项是{fbid(n)}')
except AssertionError as ae:
    print(ae)