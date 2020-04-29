'''
while 循环 中端版猜数字
data 3.30 version 3
author : Y
'''
import random	
answer = random.randint(1,100)
counter = 0
while True:
	counter += 1 
	num = float(input('请输入数字：'))
	if(num == counter):
		print('答对了!')
		break
	elif (num > counter) :
		print('数字小一点')
	elif (num < counter) :
		print('数字大一点')
print('你一共猜了 %d 次' % (counter) )