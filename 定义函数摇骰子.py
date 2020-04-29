'''
定义函数，摇色子
data 4.1 version:3
Author:Y 
'''
from random import	randint
def roll(n=2):
	"""摇色子"""
	total = 0 
	for x in range (n):
		total +=randint(1,6)
	return total

print (roll(3))