x = input("输入一个正整数：")
if x.isdigit() and int(x)>0:
    x=int(x)
    t,i=1,2
    print(x,end="")
    while t>0:
        while x%i and x!=1:
            i+=1
        if x%i==0:
            print(i,end="")
        x/=i
        t=x-i
        if x!=1:
            print("x",end="")
            while x%i and x!=1:
                i+=1
else:
    print("请输入正确的正整数！")