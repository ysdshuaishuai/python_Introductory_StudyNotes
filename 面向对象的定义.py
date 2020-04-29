class Student:
	#_init_是一个特殊方法用于在创建对象时进行初始化操作
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def study(self,coure_name):
		print(f'{self.name} 正在学习: {coure_name} .')
	def watch_movie(self,movie):
		if self.age < 18:
			print(f'{self.name} 只能看动画片')
		else:
			print(f'{self.name} 正在看电影:{movie}' )
def main():
	#创建学生对象对姓名和年龄赋值:
	stu1 = Student('ysd',190)
	#给对象发study消息：
	stu1.study('python 程序设计')
	stu1.watch_movie('阿甘正传')
if __name__ == '__main__':
	main()