'''
2.1.1 敲代码
'''
x=3
y=3.0
z="China"
list1=[1,2,3]
print(x)
print(y)
print(z)
print(list1)





'''
2.1.1举例子
'''

x=1
print(id(x))
print(type(x))
x=2
print(id(x))
print(type(x))








'''
2.2.1 敲代码
'''

a=3
b=4
c=a+b
d=a*b
print(a)
print(b)
print(c)
print(d)
a+=1
b*=2
c%=4
print(a)
print(b)
print(c)

'''
2.2.2 敲代码
'''
print(3>6)
print(5>=4)
print(5!=5)
print(4+2<3)
print("A"<"b")
print("100">"99")


'''
2.2.3 敲代码
'''
print(10>9 and  10<11)
print(2 and 3)
print(0 and 2)
print(10>9 or 10>12)
print( 2 or 3 )
print(not 4>3)






'''
2.2.4 敲代码
'''
a=[1,2,3]
b="strong"
print(1 in a)
print("st" not in b)




'''
2.2.4 敲代码
'''
print(3+4**2*2-2)
a=100
b=10
print(not a != b and a>b or b<a)






'''
2.3.1 敲代码
'''
a=123
b=-10
c=1.5e3
print(a+b)
print(a/b)
print(b//c)


'''
2.3.2字符串
str1="123"
str2="let's"
str3='
    锄禾日当午
    汗滴禾下土
    谁知盘中餐
    粒粒皆辛苦'
str4="c;\teacher\number"
print(str1+str2)
print(str1*5)
print(str3)
print(str4)
'''
sheng_xiao=['鼠','牛','虎','兔','龙','蛇','马','羊','猴','鸡','狗','猪']
id="330227200310015887"
y=id[6:10]
m=id[10:12]
d=id[12:14]
print("您生日为:",y,"",m,"",d,"")
age=2020-int(y)
sx=(int(y)-4)%12
print("今年您",age,"岁")
print("属",sheng_xiao[sx])
'''


'''
n1=eval(input("请输入本月(峰)用电度数:"))
n2=eval(input("请输入本月(谷)用电度数:"))
v1=0.538*n1+0.538*n2
v2=0.568*n1+0.288*n2
v3=12/(v1-v2)
print("传统用电计费,付",round(v1,1),"元")
print("峰谷电计算,付:",round(v2,1),"元")
print("一年下来,峰谷电节省",round(v3,1),"元")
'''

'''
cj=[]
v=eval(input("请输入第一位同学成绩:"))
cj.append(v)
v=eval(input("请输入第二位同学成绩:"))
cj.append(v)
v=eval(input("请输入第三位同学成绩:"))
cj.append(v)
v=eval(input("请输入第四位同学成绩:"))
cj.append(v)
v=eval(input("请输入第五位同学成绩:"))
cj.append(v)
v=eval(input("请输入第六位同学成绩:"))
cj.append(v)
print("六位同学成绩为",cj)
print("最高分:",max(cj))
print("最低分:",min(cj))
avg=sum(cj)/6
print("平均分:",avg)
'''

'''
list1=['sum','mon','tue','wed','thu','fri','sat']
n=int(input("请输入日期:"))
print("该天是:",list1[n%7 ])
'''

'''
list1=['z','h','o','n','g','h','u','a']
list2=['10',2,'你好']
list3=['10',(1,2,3),[1,2,3]]
print(list1)
print(list2)
print(list3)
print(list3[2])
list1[1]="b"
list2[0:2]=[3,1]
del list3[0]
list4=list1[2:4]+list2+list3[1]
print(list1)
print(list2)
print(list3)
print(list4)
'''
'''
a=123
b=-10
c=1.5e3
print(a+b)
print(a/b)
print(b//c)
'''
'''
print(10>9 and 10<11)
print(2 and 3)
print(0 and 2)
print(10>9 or 10>12)
print(2 or 3)
print(not 4>3)
'''

'''
a=3
b=4
c=a+b
d=a*b
print(a)
print(b)
print(c)
print(d)
a+=1
b*=2
c%=4
print(a)
print(b)
print(c)
'''

'''
a=123
A=456
AS="hello"
MAO=30

