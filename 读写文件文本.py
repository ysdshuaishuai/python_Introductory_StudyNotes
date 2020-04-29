import time 
def main():
	try :
		#一次性读取整个文件
		#with open ('1.txt','r',encoding = 'utf-8') as f :
		#	print (f.read())
		with open ('1.txt','r',encoding = 'utf-8') as f :
			for line in f :
				print(line , end = '')
				time.sleep(0.5)
		print()
		 
	except FileNotFoundError:
		print('无法打开指定文件！')
	except LookupError :
		print('指定了未知的编码！')
	except UnicodeDecodeError:
		print('读取文件时解码错误！')

if __name__ == '__main__':
	main()
