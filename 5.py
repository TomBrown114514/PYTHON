import time
sec = 0
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
    sec += 1
    time.sleep(1)
