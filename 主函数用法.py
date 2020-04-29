if __name__ == '__main__':#只有该模块时自动运行
    num = int(input('请输入正整数: '))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数' % num)