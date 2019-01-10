#coding=utf-8
import winsound  # 导入此模块实现声音播放功能
import time  # 导入此模块，获取当前时间
import tkinter  as tk
from tkinter import ttk
import tkinter
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


# 提示用户设置时间和分钟
my_hour = input("请输入时：")
my_minute = input("请输入分：")
my_second = input("请输入秒：")

flag = 1
root = tk.Tk()
root.title('测试窗口')
center_window(root, 300, 240)
root.maxsize(600, 400)
root.minsize(300, 240)
while flag:
    # if hour == my_hour and minute == my_minute and second == my_second:

    if  1==1:
        # music = 'test.wav'#将改wav文件放在和本文件同一个目录，路径搜索
        # winsound.PlaySound(music, winsound.SND_ALIAS)
        print("Hello World!!")
        t = time.localtime()  # 当前时间的纪元值
        fmt = "%H %M %S"
        now = time.strftime(fmt, t)  # 将纪元值转化为包含时、分的字符串
        now = now.split(' ')  # 以空格切割，将时、分放入名为now的列表中

        hour = now[0]
        minute = now[1]
        second = now[2]
        ttk.Label(root, relief=tk.FLAT,
                  text="现在时间："+hour+"时"+minute+"分"+second+"秒").pack(
            expand=tk.YES)
        root.config(bg='white')
        root.resizable(0, 0)
        root.attributes("-toolwindow", 1)
        root.wm_attributes("-topmost", 1)
        root.mainloop()
        flag = 1
