import os
import string
# 判断是否为标点符号
punc = string.punctuation # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
board_1={
    '1':'','2':'','3':'',
    '4':'','5':'','6':'',
    '7':'','8':'','9':'' 
    }
def display_board(board):
    str1=['1','2','3','4','5','6','7','8','9']
    print(' ----------')
    counter = 0
    x , y = 0 , 3
    while counter < 3 :
        for j in str1[x:y] :
            if board[j] =='':
                print(' | '+ board[j],end='')
            else :
                print(' |'+ board[j],end='')
        print(' |')
        x += 3
        y += 3
        counter += 1
        if counter >= 3:
            break
        print(' ---+--+---')
    print(' ----------')

def is_win(board):
    if  board['1'] !='' and board['1'] == board['2']  and board['2'] == board['3'] :
        return True
    elif board['4'] == board['5'] and board['5'] == board['6'] and board['4'] !='' :
        return True
    elif board['7'] == board['8'] and board['8'] == board['9'] and board['7'] !='' :
        return True
    elif board['1'] == board['4'] and board['7'] == board['4'] and board['1'] !='' :
        return True
    elif board['2'] == board['5'] and board['8'] == board['5'] and board['2'] !='' :
        return True
    elif board['3'] == board['6'] and board['9'] == board['6'] and board['3'] !='' :
        return True
    elif board['1'] == board['5'] and board['9'] == board['5'] and board['1'] !='' :
        return True
    elif board['3'] == board['5'] and board['7'] == board['5'] and board['3'] !='' :
        return True
    else:
        return False
def main():
    begin = True
    while begin :
        board = board_1.copy()
        next_1 = 'x'
        counter = 0
        is_true = True
        os.system('clear')
        display_board(board)
        while counter < 9 and True:
            while  is_true:
                move = input('\"%s\"请输入你要下的位置：  '% next_1)
                while  move in punc or int(move) > 9 or int(move) <=0:
                    print('%s输入位置超出范围，请重新输入'% next_1) 
                    move = str(input('\"%s\"请输入你要下的位置：  '% next_1))
                if board[move] == '' :
                    board[move] = next_1
                    if next_1 == 'x':
                        next_1 = 'o'
                    else :
                        next_1 = 'x'
                    break
                else :
                    print('\'%s\'输入有误，请重新输入'% next_1)
            os.system('clear')
            display_board(board)
            if is_win(board):
                break
            counter += 1
        if counter == 9:
            print("平局了。")
        else:
            if next_1 == 'x':
                print('\'o\'方 胜利！')
            else :
                print('\'x\'方 胜利！')
        choice = input('是否再次游戏：yes or no ？')
        begin = choice == 'yes'

if __name__ == '__main__':
    main()