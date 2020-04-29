"""
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险
，为了能让一部分人活下来不得不将其中
15个人扔到海里面去，有个人想了个办法
就是大家围成一个圈，由某个人开始从1报数，
报到9的人就扔到海里面，他后面的人接着从
1开始报数，报到9的人继续扔到海里面，直到
扔掉15个人。由于上帝的保佑，15个基督徒都
幸免于难，问这些人最开始是怎么站的，哪
些位置是基督徒哪些位置是非基督徒。
""" 
def  main():
	persons = [0]*30
	counter,index,number=0,0,0
	while  counter <15 :
		if persons[index] == 0:
			number  += 1
			if number == 9:
				persons[index] = 1
				counter += 1
				number = 0
		index += 1
		index %= 30
	for person in persons:
		if person == 0:
			print('基督 ',end="")
		else:
			print('非基督 ',end="")
						
if __name__ == '__main__':
    main()