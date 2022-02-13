"""
使用tkinter设计并制作一个菜单:实现在文本框中输入姓名单机“提交”按钮,
即可在“已经提交”处显示已经提交的姓名
单击“清空”即可将刚才输入的姓名从文本框中清除
"""
from tkinter import *
guo = Tk()
guo.title("提交姓名")
guo.geometry("250x250")
s=""
def sclear():
    tex1.delete(0,END)
def pu():
    f=tex1.get()
    global s
    s = s + f + " "
    Label(guo,text=s).grid(row=2,column=1,sticky=W)
lab=Label(guo,text="姓名:")
lab.grid(row=0,column=0,sticky=W)
tex1=Entry(guo,state=NORMAL,width=20)
tex1.grid(row=0,column=1)
Button(guo,text="清空",command=sclear)\
    .grid(row=1,column=0,sticky=W,pady=10)
Button(guo,text="提交",command=pu)\
    .grid(row=1,column=1,sticky=W,pady=10)
Label(guo,text="已经提交:").grid(row=2,column=0)
guo.mainloop()