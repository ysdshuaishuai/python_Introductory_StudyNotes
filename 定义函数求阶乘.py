'''
定义函数，求阶乘
身份验证 day3
data 4.1 version:3
Author:Y 
'''
def factorial (num):
	res=1
	for n in range(1,num+1):
		res *=n
	return res	

m = int(input('m = '))
n = int(input('n = '))
print ('%d 的阶乘是：%d' % (m,factorial(m)))
print ('%d 的阶乘是：%d' % (n,factorial(n)))