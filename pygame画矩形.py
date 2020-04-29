import pygame 
from pygame.locals import *
from math import *
def main():
	# 初始化导入pygame中的模块
	pygame.init() 
	#初始化用于显示窗口的大小
	screen = pygame.display.set_mode((500,500)) 
	#设置窗口的标题
	pygame.display.set_caption('井字棋')
	#设置窗口背景颜色(红绿蓝)
	screen.fill((208,104,0))
	#绘制一个矩形(屏幕，颜色，Rect:左上角的坐标:(200,5),宽度和高度:(100,100)，粗细)
	pygame.draw.rect(screen, (0,0,0), ((8, 8), (480, 480)), 5)
	for x in range(160,480,160):
		pygame.draw.line(screen,(0,0,0),(8,x),(485,x),5)
		for y in range(160,480,160):
			pygame.draw.line(screen,(0,0,0),(y,8),(y,485),5)
	#刷新当前窗口(将绘制的图像呈现出来)
	pygame.display.flip()
	running = True 
	#开启一个事件循环处理发生的时间
	while running:
		#从消息队列中获取事件并对事件进行处理：
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		
			elif event.type == MOUSEBUTTONUP:
			#获得鼠标位置
				x , y = pygame.mouse.get_pos()
			#计算光标的左上角的位置
				a = x-int(screen.get_width()/2)
				b = y-int(screen.get_height()/2)
				c = int(sqrt(x*x+y*y))
			#把光标画上去	
				pygame.draw.circle(screen, (255, 0, 0,), (a, b),c, 1)
		#刷新画面

		pygame.display.update()
		

if __name__ == '__main__':
	main()