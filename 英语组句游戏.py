from tkinter import *
guo = Tk()
guo.title("英语组句游戏")
guo.geometry("240x120")
tex=Text(guo,width=30,height=50)
tex.grid(row=0,column=0)
tex.tag_config("tag_1",background="yellow",foreground="red")
def insert_b1():
    tex.insert("insert","I love ")
def end_b2():
    tex.insert("end","python","tag_1")
def dele_b3():
    tex.delete(0.0,END)
Button(tex,text="I love ",command=insert_b1).grid(row=0,column=1,padx=20,pady=20,sticky=S)
Button(tex,text="python",command=end_b2).grid(row=0,column=2,padx=0,pady=0,sticky=S)
Button(tex,text="删除文本",command=dele_b3).grid(row=0,column=3,padx=20,pady=20,sticky=S)
guo.mainloop()