# 斐波那契数列 中 yield 的用法 
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a 
       '''不停止循环 返回值，下一次从返回处继续
进行循环'''

def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()