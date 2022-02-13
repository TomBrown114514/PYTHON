import re  # 导入正则库

Str = input("请输入一段字符：")
Dict = {"中英文": 0, "数字": 0, "空格": 0, "其他": 0}
CE = re.compile(r'^[\u4E00-\u9FA5]|[A-Z]|[a-z]$')
# 定义一个正则表达式，用于判断中英文字符
N = re.compile(r'[0-9]')  # 定义一个正则表达式，用于判断数字
for i in Str:
    if re.match(CE, i):  # 正则表达式匹配
        Dict["中英文"] += 1
    elif re.match(N, i):  # 正则表达式匹配
        Dict["数字"] += 1
    elif i == " ":
        Dict["空格"] += 1
    else:
        Dict["其他"] += 1
# 输出结果
for x, y in Dict.items():
    print(f'{x}字符：{y}')
