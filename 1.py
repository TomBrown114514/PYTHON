import time

d = int(input("请输入天数："))
h = int(input("请输入小时："))
m = int(input("请输入分钟："))
s = int(input("请输入秒钟："))

sec = d*86400+h*3600+m*60+s

while True:
    D = sec//86400
    H = (sec%86400)//3600
    M = ((sec-D*86400)%3600)//60
    S = sec%60
    
    if D!=0:
        print("{}:{:02}:{:02}:{:02}".format(D,H,M,S))
    elif D==0 and H!=0:
        print("{:02}:{:02}:{:02}".format(H,M,S))
    elif D==0 and H==0 and M!=0:
        print("{:02}:{:02}".format(M,S))
    elif D==0 and H==0 and M==0 and S!=0:
        print("{:02}".format(S))
    if sec == 0:
        break
    else:
        sec -= 1
    time.sleep(1)
