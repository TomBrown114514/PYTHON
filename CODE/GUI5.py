from tkinter import *
win = Tk()
win.title("我的设计")
win.geometry("300x300")
group = LabelFrame(win,text="我喜欢的语言？",padx=5,pady=5)
group.pack(padx=10,pady=10)
LANGES = [("python",1),("vb",2),("C",3),("C#",4)]
v=IntVar()
v.set(1)
for lang,num in LANGES:
    b=Radiobutton(group,text=lang,variable=v,value=num)
    b.pack(anchor=W)
win.mainloop()