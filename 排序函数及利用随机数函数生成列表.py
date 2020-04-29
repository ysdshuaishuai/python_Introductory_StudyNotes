'''
排序函数 及 利用随机数函数生成列表
'''
import random 
def max_maxsen(x):
	m1,m2 = (x[0],x[1]) if x[0] > x[1] else (x[1],x[0])
	for index in range(2,len(x)):
		if x[index] > m1:
			m2 = m1
			m1 = x[index]
		elif x[index] > m2:
			m2 = x[index]
	return m1,m2
def list_creat():
	x = list(random.randint(1,1000) for i in range(0,10) )	
	return x
def list_creat_1():
	x = []
	count = 0
	while count < 10:
		x.append(random.randint(1,999)) 
		count +=1
	return x
if __name__ == '__main__':
	x=list_creat()
	print(x,end=" ")
	print(max_maxsen(x))
	y=list_creat_1()
	print(y," ",max_maxsen(y))