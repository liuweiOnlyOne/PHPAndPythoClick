#coding=gbk
import win32api
import win32con
from ctypes import *
import time

tt = '03'
flag = 1
while flag:
	t = time.localtime()  # ��ǰʱ��ļ�Ԫֵ
	fmt = "%H %M %S"
	now = time.strftime(fmt, t)  # ����Ԫֵת��Ϊ����ʱ���ֵ��ַ���
	now = now.split(' ')  # �Կո��и��ʱ���ַ�����Ϊnow���б���

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