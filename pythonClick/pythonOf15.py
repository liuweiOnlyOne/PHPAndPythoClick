#coding=gbk
#��������200�д������ң�ʵ����һ��ʱ�ӵĳ��򣬲��ҽ�����Pthon���Զ�����ʱ�����ť�Ĺ���ʵ�֣�ʵ���˿���������
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