# -*- coding: utf-8 -*-
from tkinter import *
# 引入字体模块
import tkinter.font as tkFont

root = Tk()
# 创建一个Label
# 指定字体名称、大小、样式
ft = tkFont.Font(family='Fixdsys', size=40, weight=tkFont.BOLD)
ft1 = tkFont.Font(size=20, slant=tkFont.ITALIC)
ft2 = tkFont.Font(size=30, weight=tkFont.BOLD, underline=1, overstrike=1)

Label(root, text='thist is a demo', font=ft).grid()
Label(root, text='hello python ', font=ft1).grid()
Label(root, text='good luck', font=ft2).grid()

root.mainloop()
# 使用tkFont.Font来创建字体。
