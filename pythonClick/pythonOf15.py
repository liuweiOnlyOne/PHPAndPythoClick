#coding=gbk
#又新增了200行代码左右，实现了一个时钟的程序，并且进行了Pthon的自动化定时点击按钮的功能实现，实现了开机自启动
import win32api
import win32con
from ctypes import *
import time

tim1 = "00"
tim2 = "15"
tim3 = "30"
tim4 = "45"
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
	if minute==tim1 and second==tt:
		for i in range(1,2):
			# time.sleep(1)
			windll.user32.SetCursorPos(1100,600);
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,1100, 600)
			time.sleep(0.05)
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 1100, 600)
		flag = 1
	if minute==tim2 and second==tt:
		for i in range(1,2):
			# time.sleep(1)
			windll.user32.SetCursorPos(1100,600);
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,1100, 600)
			time.sleep(0.05)
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 1100, 600)
		flag = 1
	if minute==tim3 and second==tt:
		for i in range(1,2):
			# time.sleep(1)
			windll.user32.SetCursorPos(1100,600);
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,1100, 600)
			time.sleep(0.05)
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 1100, 600)
		flag = 1
	if minute==tim4 and second==tt:
		for i in range(1,2):
			# time.sleep(1)
			windll.user32.SetCursorPos(1100,600);
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,1100, 600)
			time.sleep(0.05)
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 1100, 600)
		flag = 1