# 8 Q54
f = open("guo.txt","w")
i=0
while i<=4:
    w=1
    while w <= 4+i: 
        f.write(str(w)+" ")
        w=w+1
    f.write("\n")
    i=i+1
f.close()
f=open("guo.txt")
pt=[]
for line in f:
    pt.append(line.strip("\n").strip(""))
f.close()
f=open("guo.csv","w")
for row in pt:
    f.write(",".join(row)+"\n")
f.close()