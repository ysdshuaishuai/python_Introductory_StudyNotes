'''
输入一个正整数判断是否为素数
身份验证 day3
data 3.31 version:3
Author:Y 
'''
num = int(input('请输入一个正整数： '))
while num > 0:
	counter = 0
	for x in range (2,num):
		if num % x ==0:
			counter+=1
			break
	if counter ==0 and num !=1:
		print('%d 是一个素数' % num)
	else:
		print('%d 不是一个素数' % num)
	num = int(input('请输入一个正整数： '))
