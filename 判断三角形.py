'''
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积
data 3.30 version 3
author : Y
'''
print('请输入三角形三边长a,b,c :')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a+b>c and a+c>b and b+c>a:
	print('该三角形周长为：%.2f' %(a + b + c))
	p = (a + b + c) / 2
	area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
	print('该三角形的面积为： %.2f' %(area))
else:
	print('该三角形不能被构成')
