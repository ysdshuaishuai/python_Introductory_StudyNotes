'''
***矩阵***
身份验证 day3
data 3.31 version:3
Author:Y 
'''
l = int(input('请输入行数： '))
for i in range(l):
	for _i in range(0,i+1):
		print('*',end="")
	print()
l = int(input('请输入行数： '))
for j in range(l):
	for _j in range(0,l-j-1):
		print(' ',end='')
	for __j in range(0,j+1):
		print("*",end='')
	print()
l = int(input('请输入行数： '))
for i in range(l):
    for _ in range(l - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()	