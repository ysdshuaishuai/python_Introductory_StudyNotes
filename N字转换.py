def f(s,numRows):  
    if numRows == 1:
            return s
    words = ['' for i in range(numRows)]
    print(words)
    p = 0
    for i in s:
        if p == 0:
            flag = 1
        elif p == numRows - 1:
            flag = -1
        words[p] += i
        p += flag
        print(''.join(words))
    return ''.join(words)
if __name__ == '__main__':
    
    print(f('LEETCODEISHIRING',3))