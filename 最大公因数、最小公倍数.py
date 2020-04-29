'''
最大公因数，最小公倍数
身份验证 day3
data 3.31 version:3
Author:Y 
'''
x = int(input('x = '))
y = int(input('y = '))
if x >y:
	x,y = y,x
for z in range(x,0,-1):
	if x % z==0 and y%z==0:
		break
if z != 0 : 
	print('%d和%d的最大公因数为：%d'% (x,y,z))
	print('%d和%d的最小公倍数是:%d' % (x, y, x * y //z))