import pygame

SIZE = [800,600]
GAMENAME = "First game"

BLACK	= (0  ,0  ,0  )
WHITE	= (255,255,255)
RED		= (255,0  ,0  )
GREEN	= (0  ,255,0  )
BLUE	= (0  ,0  ,255)
GRAY	= (100,100,100)
LGRAY	= (150,150,150)
CLEAR	= (0  ,0  ,0  ,0)


pygame.init()

window = pygame.display.set_mode(SIZE)
pygame.display.set_caption(GAMENAME)

backLay = pygame.Surface(SIZE)
foreLay = pygame.Surface(SIZE,pygame.SRCALPHA)

backLay.fill(BLUE)
foreLay.fill(CLEAR)

square = pygame.Surface([40,40])
square.fill(RED)

x = 0

moveRight = True

while True:
	backLay.fill(BLUE)
	foreLay.fill(CLEAR)

	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			pygame.quit()


	if x>360:
		moveRight=False
	elif x<0:
		moveRight=True
	
	if moveRight:
		x+=1
	else:
		x-=1


	foreLay.blit(square,[x,x])

	window.blit(backLay,[0,0])
	window.blit(foreLay,[0,0])
	pygame.display.flip()
	pygame.time.delay(5)
