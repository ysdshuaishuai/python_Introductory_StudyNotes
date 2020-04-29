'''
字典的用法
'''
scores = {'ysd' : 95 , 'hxd' : 78 , 'gkd' : 82}
print (scores)
#创建字典的构造器语法
items1 = dict(one = 1 , two = 2 , three = 3 , four = 4)
#通过zip函数将两个序列压成字典
items2 = dict(zip(['a','b','c'],'1234'))
#闯将字典的推导式语法
items3 = {num : num ** 2 for num in range (1,10)}
print(f'{items1} \n {items2} \n {items3}')
#
de = ['w' , 'a', 'n']
it = list(num * 2 for num in range (1,10))
items4 = dict(zip(de,it))
print (items4)
#通过键可以获取字典中的对应值
print(scores['ysd'])
print(scores['hxd'])
#对字典中的所有键值进行遍历
for key in scores:
	print(f'{key} : {scores[key]}')
#更新字典中的元素
scores['hxd'] = 100
scores['ysd'] = 101
scores.update(why = 85  , data= 99)
print (scores)
if 'ysd' in scores:
	print('ysd :' ,scores['ysd'])
print(scores.get('hxd')) 
#get方法也是通过键获取对应的值但是可以设置默认值get('Xxx',60)
#删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('ysd',100))
print(scores)
#清空列表
scores.clear()
print(scores)
