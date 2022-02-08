def division():
    """功能:分苹果"""
    print("\n==================== 分苹果了 ==================== \n")
    apple = int(input("请输入苹果的个数:")) #输入苹果的个数
    children = int(input("请输入来了几个小朋友:"))
    assert apple > children, "苹果不够分" #应用断言测试
    assert children > 0, "不能被零或负数个人分!" 
    result = apple // children #计算每个人分几个苹果
    remain = apple % children #计算余下的几个苹果
    print(f"{apple}个苹果,平均分给{children}个小朋友,每人分{result}个,剩下{remain}个" if remain > 0\
        else f"{apple}个苹果,平均分给{children}个小朋友,每人分{result}.")

if __name__ == "__main__":
    try:
        division()
    except AssertionError as e:
        print("\n输入有误:",e)