'''
9*9乘法表
身份验证 day3
data 3.30 version:3
Author:Y 
'''
for x in range(1,10):
	if(x==1):
		print(' |------------|')
	else:
		print('|------------|')
	for y in range(1,10):
		if x*y<10:
			print(' |(%d * %d = %d' %(x,y,(x*y)),end=') | ')
		else:
			print(' |(%d * %d = %d' %(x,y,(x*y)),end=')| ')
		print(end='\n')
	print(end=' ')
print('|------------|')


		
  