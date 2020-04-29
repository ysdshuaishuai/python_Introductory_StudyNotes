#计算指定的年月日是这一年的第几天。
def is_leap_year(year):
 	return  year % 4 == 0 and year % 100 != 0 or \
 	year % 400 == 0
def which_day(year,month,day):
	day_of_month = [
	[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
	[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	][is_leap_year(year)]
	total = 0
	for index in range (month-1):
		total += day_of_month[index]
	return total+day
if __name__ == '__main__':
	year,month,day = map(int,input('请输入年月日：').split(' '))
	#利用map函数///map(int,input().split(' '))\\\split()(括号里可以填分界符号)以什么为分界输入n个数
	while year > 0 and month > 0 and day > 0:	
		whday = which_day(year,month,day)
		print(f'{year}-{month}-{day}.是 {year} 年的第: {whday} 天。')
		year,month,day = map(int,input('请输入年月日：').split(' '))