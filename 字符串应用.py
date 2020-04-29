'''
字符串 应用；
data 4.1 version:3
Author:Y 
'''
s1 = '\'hello, world!\''  #\ -> 进行转义
s2 = '\n\\hello, world!\\\n'# \n 换行
print(s1, s2, end='')  
s1 = '\141\142\143\x61\x62\x63' #abcabc
s2 = '\u9a86\u660a' 
print(s1, s2)
s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')