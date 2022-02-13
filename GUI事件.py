from tkinter import *
def a(event):
    hello.config(text="欢迎使用本系统",bg="white",fg="black")
def b(event):
    hello.config(text="欢迎下次再来",fg="blue",bg="red")
fuck = Tk()
hello = Label(fuck,text="欢迎进入程序空间",font=("隶书",15))
hello.pack()
Button(fuck,text="退出",command=fuck.destroy).pack()
fuck.bind("<Enter>",a)
fuck.bind("<Leave>",b)
fuck.mainloop()