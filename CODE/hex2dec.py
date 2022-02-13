#十进制转换为十六进制
base = [str(x) for x in range(10)] + [chr(x) for x in range(ord("A"), ord("A") + 6)]


def DEC_TO_HEX(num):
    '''
    将十进制转换为十六进制。
    :param num:十进制的数
    :return:十六进制的数
    '''
    l = []
    if num < 0:
        return "-" + DEC_TO_HEX(abs(num))
    while 1:
        num, rem = divmod(num, 16)
        l.append(base[rem])
        if num == 0:
            return "".join(l[::-1])


DEC = int(input("请输入一的十进制的数字："))
print(f"转换为十六进制为：{DEC_TO_HEX(DEC)}")