'''
身份验证 day3
data 3.30 version:3
Author:Y 
'''
username =  str(input('请输入用户名 :'))
password = str(input('请输入密码 :'))
# 用户名为admin 密码为 123456
if username == 'admin' and \
   password =='123456':
	print("身份验证成功！")
else:
	print("身份验证失败！")