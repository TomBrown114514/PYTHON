from tkinter import *

def fuck():
    dhks = Tk()
    dhks.title("语言")
    dhks.geometry("150x150")
    Label(dhks,text=f"你选择的是{Lang.get()}！").pack(expand=YES)
    Button(dhks,text="确定",command=dhks.destroy).pack(anchor=S)
    dhks.mainloop()

win = Tk()
win.title("编程语言")
win.geometry("250x250")
Label(win,text="选择一门你喜欢的编程语言").pack(anchor=W)
Lang = StringVar()
Radiobutton(win,text="Python",variable=Lang,value="Python",command=fuck).pack(anchor=W)
Radiobutton(win,text="C++",variable=Lang,value="C++",command=fuck).pack(anchor=W)
Radiobutton(win,text="C",variable=Lang,value="C",command=fuck).pack(anchor=W)
Radiobutton(win,text="Java",variable=Lang,value="Java",command=fuck).pack(anchor=W)
win.mainloop()