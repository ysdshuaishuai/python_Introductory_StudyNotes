'''
格式化输出字符串
data 4.1 version:3
Author:Y 
'''
a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
print('{0} * {1} = {2}'.format(a, b, a * b))#字符串提供的方法来完成字符串的格式
print(f'{a} * {b} = {a * b}')#字符串前加上字母f，我们可以使用下面的语法