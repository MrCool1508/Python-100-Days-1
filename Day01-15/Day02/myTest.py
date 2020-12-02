'''
file: myTest.py
author: hzy
version: V1.0.0
date: 2020-12-02 23:14:52
brief: 模块目的、功能
History: 
<author><date><version><brief>
'''
# a = 321
# b = 123
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)
# c = int(input("please enter your num ="))
# d = int(input("yo ="))
# print(c+d)

import math
# Practice
# No.1 摄氏温度华氏温度相互转换

f = float(input("请输入华氏温度F = "))
c = (f-32)/1.8
print("摄氏温度为C = %.1f" % c)
# No.2 输入圆的半径计算周长和面积
radius = float(input("请输入圆的半径r = "))
circle = 2 * math.pi * radius
area = math.pi * radius ** 2
print("周长为：%.1f，面积为：%.2f" % (circle, area))
# No.3 判断输入的年份是否为闰年
year = int(input("请输入需要判断的年份："))
isLeap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
print(isLeap)
