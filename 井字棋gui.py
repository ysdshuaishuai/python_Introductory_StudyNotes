import pygame
import random

class chess():
	chess_arr = [] # 储存落在棋盘上的棋子。
	game_state = 1 # 1 为正常进行 2 为X获胜 3 为O获胜
	flag = 1 # 定义X O 的轮次 1：X 2：O
	
	def init_board(self):
		pygame.init()
		space = 60
		cell_size = 100
		cell_nums = 4
		board_size = cell_size * (cell_nums-1) + space * 2
		screencaption = pygame.display.set_caption('井字棋')
		screen = pygame.display.set_mode((board_size,board_size))
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT :
					pygame.quit()
					exit()
				elif self.game_state ==1 and event.type == pygame.MOUSEBUTTONUP: #鼠标弹起
					x , y = pygame.mouse.get_pos() # 获取鼠标位置
					xi = int ((x - space)*1.0/cell_size)
					yi = int ((y - space)*1.0/cell_size)
					if xi >= 0 and xi < cell_nums-1 and yi >= 0 and yi < cell_nums-1 and (xi,yi, 1) not in self.chess_arr and (xi,yi, 2) not in self.chess_arr:
						self.chess_arr.append((xi,yi,self.flag))
						if self.check_win():
							if self.flag == 1 :
								self.game_state = 2 
							else:
								self.game_state = 3
						else:
							if self.flag == 1 :
								self.flag = 2
							else:
								self.flag = 1 
						print(xi,yi,self.flag,self.game_state)		
			screen.fill((208,104,0))		
			for x in range(0,cell_size*cell_nums,cell_size):
				pygame.draw.line(screen,(0,0,0),(x+space,0+space),(x+space,cell_size*(cell_nums-1)+space),5)
			for y in range(0,cell_size*cell_nums,cell_size):
				pygame.draw.line(screen,(0,0,0),(0+space,y+space),(cell_size*(cell_nums-1)+space,y+space),5)
			for xi , yi ,zi in self.chess_arr:
				if zi == 1:
					pygame.draw.line(screen,(0,0,0),(xi*cell_size+space,yi*cell_size+space),((xi+1)*cell_size+space,(yi+1)*cell_size+space),8)
					pygame.draw.line(screen,(0,0,0),((xi+1)*cell_size+space,yi*cell_size+space),(xi*cell_size+space,(yi+1)*cell_size+space),8)
				else:
					pygame.draw.circle(screen,(0,0,0),(xi*cell_size+space+50,yi*cell_size+space+50),50,5)
		 	
			if self.game_state !=1:
		 		myfont = pygame.font.Font(None,50)
		 		red = 255,0,0
		 		win_text = "\'%s\'  win!! ,  you are loser !" %('X' if self.game_state == 2 else 'O' )
		 		text = myfont.render(win_text,True,red)
		 		screen.blit(text,(20,190))
			if self.game_state ==1 and len(self.chess_arr) == 9:
				myfont = pygame.font.Font(None,50)
				red = 255,0,0
				win_text = "It's a draw ."  
				text = myfont.render(win_text,True,red)
				screen.blit(text,(20,190))
			pygame.display.update()
		
	def check_win(self):
		chess_data = [[0]*3 for index in range (0,3)] # 定义棋盘的棋子下落情况 不能用 [[0]*3]*3  单个棋子的摆放会被重复赋值
		for x , y , z in self.chess_arr :
			if z == self.flag :
				chess_data [y][x] = 1
				
		lx = self.chess_arr[-1][0]
		ly = self.chess_arr[-1][1]
		w_data = [[(-1,0),(1,0)],[(0,-1),(0,1)],[(-1,-1),(1,1)],[(-1,1),(1,-1)]] #判断获胜的四个方向
		
		for de1 , de2 in w_data:
 			dx , dy = de1
 			num1 = self.get_cell_nums(lx,ly,dx,dy,chess_data)
 			dx , dy = de2
 			num2 = self.get_cell_nums(lx,ly,dx,dy,chess_data)
 			if num1 + num2 + 1 >= 3 :
 				print(num1+num2)
 				return True
		return False

	def get_cell_nums(self,lx , ly , dx , dy ,c):
		tx , ty = lx , ly 
		s = 0
		while True:
			tx += dx
			ty += dy
			if  tx < 0 or tx >= 3 or ty < 0 or ty >= 3 or c[ty][tx] == 0 : 
				return s 
			s += 1

	def  p(self):
		print('hello')


def main():
	A = chess()
	A.init_board()

if __name__ == '__main__':
	main()
