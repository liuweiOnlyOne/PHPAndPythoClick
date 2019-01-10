#coding=gbk
import win32api
import win32con
from ctypes import *
import time

tt = '03'
flag = 1
while flag:
	t = time.localtime()  # 当前时间的纪元值
	fmt = "%H %M %S"
	now = time.strftime(fmt, t)  # 将纪元值转化为包含时、分的字符串
	now = now.split(' ')  # 以空格切割，将时、分放入名为now的列表中

	hour = now[0]
	minute = now[1]
	second = now[2]
	time.sleep(0.5)
	print(second)
	print(second == tt)
	if second==tt:
		for i in range(1,2):
			# time.sleep(1)
			windll.user32.SetCursorPos(1100,600);
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,1100, 600)
			time.sleep(0.05)
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 1100, 600)
		flag = 1