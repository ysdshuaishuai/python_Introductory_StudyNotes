'''
集合的使用
'''
# 创造集合的字面量语法
set1 = {1,2,3,3,3,2}
print(set1)
print('Length:', len(set1))
#创造集合的构造器语法
set2 = set(range(1,10)) 
set3 = set((1,2,3,3,2,1))
# set() 创造一个无序不重复的元素集，可进行关系测试
#删除重复数据，话可以计算交集，差集，并集等
print(set2,set3)
set4 = {num for num in range (1,100) if num %3\
== 0 or num % 5 == 0}
print(set4)
set1.add(4)
set1.add(5)
#set2.updata([11])#updata 更新集合中的元素 有合并字典删除相同项的作用
set2.discard(5)
if 4 in set2:
	set2.remove(4)
print(set1,set2)
print(set3.pop())
print(set3)
# 集合的交集、并集、差集、对称差运算
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))
# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))