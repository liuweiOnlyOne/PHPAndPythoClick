# import tkinter.messagebox
# from tkinter import *
# tkinter.messagebox.askokcancel("FishC Demo",'发射导弹？')
# tkinter.messagebox.askquestion("FishC Demo","买个优盘？")
# tkinter.messagebox.askretrycancel("FishC Demo","启动失败，重试？")
# tkinter.messagebox.askyesno("FishC Demo","我帅吗?")
# tkinter.messagebox.showerror("FishC Demo","出错啦！")
# tkinter.messagebox.showinfo("FishC Demo","2017新年快乐")
# tkinter.messagebox.showwarning("FishC Demo","你在偷懒！")
#
# def but():
#     tkinter.messagebox.showinfo('提示', '人生苦短')
#     #tkinter.messagebox.showwarning('警告', '明日有大雨')
#     #tkinter.messagebox.showerror('错误', '出错了')
# root=tkinter.Tk()
# root.title('GUI')#标题
# root.geometry('800x600')#窗体大小
# root.resizable(False, False)#固定窗体
# tkinter.Button(root, text='hello button',command=but).pack()
# root.mainloop()

import tkinter  as tk
from tkinter import ttk


def get_screen_size(window):
    return window.winfo_screenwidth(), window.winfo_screenheight()


def get_window_size(window):
    return window.winfo_reqwidth(), window.winfo_reqheight()


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    print(size)
    root.geometry(size)


root = tk.Tk()
root.title('测试窗口')
center_window(root, 300, 240)
root.maxsize(600, 400)
root.minsize(300, 240)
ttk.Label(root, relief=tk.FLAT, text='屏幕大小(%sx%s)\n窗口大小(%sx%s)' % (get_screen_size(root) + get_window_size(root))).pack(
    expand=tk.YES)
tk.mainloop()