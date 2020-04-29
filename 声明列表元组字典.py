# 声明列表
it0 = [1,2,3,4,5,6,7,8,9,0]
print
it1 = list(num * 2 for num in range (1,10))
print (it1)
it2 = [x * y  for x in (1,10) for y in range (1,10) ]
print (it2)
x = list(random.randint(1,1000) for i in range(0,10) )
print(x)
# 声明元组
it3 = (1,2,3,4,5,6,7,8,9,0)
it4 = tuple(num * 2 for num in range (1,10))
print(it4)
it5 = tuple(it1)
print(it5)
it5 = list(it1)
print(it5)
# 声明字典
it6 = {'ysd' : 95 , 'hxd' : 78 , 'gkd' : 82}
it7 = ['zrf','wtf']
it8 = [x**3 for x in range (1,3)]
print (f'{it6} \n {it7} \n {it8}')
it9 = dict(zip (it7,it8))
print(it9)