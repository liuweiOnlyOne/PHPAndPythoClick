# coding=utf-8

import _tkinter
import tkinter.messagebox
tkinter.messagebox.askokcancel('提示','这是一个消息框')
def show():
    tkinter.messagebox.showinfo(title='aaa', message='bbb')


def creatfram():
    root = tkinter.Tk()
    b = tkinter.Button(root, text="关于", command=show)
    b.pack()
    root.mainloop()


creatfram()