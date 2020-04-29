'''
百分制成绩转换为等级制成绩
data 3.30 version
author : Y
'''
score = float(input('请输入成绩： '))
if score >= 90:
	garde = 'A'
elif score < 90 and score >=80:
	garde = 'B'
elif score <80 and score >=70:
	garde= 'C'
elif score <70 and score >=60:
	garde='D'
else:	
	garde='E'
print('该成绩的等级为：',garde)

