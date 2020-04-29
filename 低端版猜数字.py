'''
低端版猜数字
身份验证 day3
data 3.30 version:3
Author:Y 
'''
print ("hello world\n")
temp = int (input("猜数字\n"))
while  temp>=0:
             guess = int (temp)
             if guess ==8 :
                 print ("卧槽 对了")
                 print ("牛逼")
             else:
                 print ("傻逼，猜错了")
                 print ("Game over")
             temp = int (input("猜数字\n")) 
print("gg")