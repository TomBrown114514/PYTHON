from tkinter import *
guo=Tk()
guo.title("学科作业完成情况")
guo.geometry("400x300")
Label(guo,text="学科作业完成情况").pack()
listbox= Listbox(guo)
listbox.insert(1,"语文")
listbox.insert(2,"数学")
listbox.insert(3,"英语")
listbox.insert(4,"Python")
listbox.pack()
Button(guo,text="完成",command=lambda listbox = listbox:listbox.delete(ANCHOR)).pack()
guo.mainloop()