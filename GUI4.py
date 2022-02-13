from tkinter import *
guo = Tk()
guo.title("编程语言")
guo.geometry("250x250")
language=[('Python',0),("C++",1),("C",2),("Java",3)]
v=IntVar()
def call():
    for i in range(4):
        if v.get() == i:
            root1=Tk()
            root1.title("语言")
            root1.geometry("150x150")
            Label(root1,text="你的选择是"+language[i][0]+"!",fg="red",width=20,height=6).pack()
            Button(root1,text="确定",width=3,height=1,command=root1.destroy).pack(side=BOTTOM)
Label(guo,text="选择一门你喜欢的编程语言").pack(anchor=W)
for lan,num in language:
    Radiobutton(guo,text=lan,value=num,command=call,variable=v).pack(anchor=W)
guo.mainloop()