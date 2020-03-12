import pygame
SIZE = [800,600]
GAMENAME = "First game"


BLACK	= (0,0,0)
WHITE	= (255,255,255)
RED		= (255,0,0)
GREEN	= (0,255,0)
BLUE	= (0,0,255)
GREY	= (100,100,100)
LGREY	= (150,150,150)
CLEAR	= (0, 0, 0, 0)

pygame.init()
window = pygame.display.set_mode(SIZE) #setmode указать режим дисплея, отображаемоей области
pygame.display.set_caption(GAMENAME)

backLay = pygame.Surface(SIZE) #площадь-поверхность-плоскость 
foreLay = pygame.Surface(SIZE, pygame.SRCALPHA)

backLay.fill(BLUE)
foreLay.fill(CLEAR)

#обьект, но тоже поверхность
square = pygame.Surface([40,40])
square.fill(RED)
x = 0
y = 0

moveRight = True

pygame.key.set_repeat(1,0)
while True:
	backLay.fill(BLUE) #очистка экрана
	foreLay.fill(CLEAR)

	for e in pygame.event.get(): #get функция возващает события произошедшие за предыдущий кадр
		if e.type == pygame.QUIT:
			pygame.quit()
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_LEFT:
				x-=1
			if e.key == pygame.K_RIGHT:
				x+=1
			if e.key == pygame.K_UP:
				y-=1
			if e.key == pygame.K_DOWN:
				y+=1
	
	
	foreLay.blit(square,[x,y])

	window.blit(backLay,[0,0]) 
	window.blit(foreLay,[0,0])
	pygame.display.flip()
	pygame.time.delay(5)











