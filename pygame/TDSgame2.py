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
square1 = pygame.Surface([40,40]) #ВОТ ТУТ ВОЗНИК ВОПРОС, А КАК МЫ СВЯЗЫВАЕМ ДЕЙСТВИЯ С ОБЬЕКТОМ??? Т.Е. ЧТО ЗАСТАВЛЯЕТ НАШУ ПОВЕРХНОСТЬ ДВИГАТЬСЯ
square.fill(RED)
x1 = 0
y1 = 0

moveRight = True

square2 = pygame.Surface([40,40])
square.fill(GREY)
x2 = 100
y2 = 0

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
				x1-=1
			if e.key == pygame.K_RIGHT:
				x1+=1
			if e.key == pygame.K_UP:
				y1-=1
			if e.key == pygame.K_DOWN:
				y1+=1

	for e2 in pygame.event2.get(): #get функция возващает события произошедшие за предыдущий кадр
		
		if e2.type == pygame.KEYDOWN:
			if e2.key == pygame.K_a:
				x2-=1
			if e2.key == pygame.K_d:
				x2+=1
			if e2.key == pygame.K_w:
				y2-=1
			if e2.key == pygame.K_s:
				y2+=1
	
	
	foreLay.blit(square1,[x1,y1])

	foreLay.blit(square2,[x2,y2])

	window.blit(backLay,[0,0]) 
	window.blit(foreLay,[0,0])
	pygame.display.flip()
	pygame.time.delay(5)











