'''
数学分段函数
data 3.30 version 3
Author : Y
'''
print('        _         ')
print('       | 3x-5 (x > 1)')
print('f(x) = | x+2  (-1 <= x <= 1)')
print('       |_ 5x+3 (x < -1)')
print('        ')
x = float(input('请输入 x = '))
if x > 1:
	num = 3*x-5
elif x >= -1 and x <= 1:
	num = x+2
elif x < -1:
	num = 5*x+3
print('f(%.2f) =%.2f ' % (x,num))
