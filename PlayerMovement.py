import pygame
pygame.init()

win =pygame.display.set_mode((500, 500))
pygame.display.set_caption("Player Movement")
clock = pygame.time.Clock()

height = 50
width = 50
x = 500/2
y = 500/2
speed = 10
jump = False
jumpCount = 10

run = True


class characters(object):
	def __init__(self,height,width,x,y,speed,jump,jumpCount):
		self.height = height
		self.width = width
		self.x = x
		self.y = y
		self.speed = speed
		self.jump = jump
		self.jumpCount = jumpCount

""" Basic Player Movement
while run:
	clock.tick(30)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	keys = pygame.key.get_pressed()
	if keys[pygame.K_a]:
		x -= speed

	if keys[pygame.K_d]:
		x += speed

	if keys[pygame.K_w]:
		y -= speed

	if keys[pygame.K_s]:
		y += speed
	win.fill((0,0,0))
	pygame.draw.rect(win, (255,0,0), (x, y, width, height))
	pygame.display.update()
    
pygame.quit()
"""
""" Basic Player Movement Jumping
while run:
	clock.tick(30)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	keys = pygame.key.get_pressed()
	if keys[pygame.K_a]:
		x -= speed

	if keys[pygame.K_d]:
		x += speed
	if not(jump):
		if keys[pygame.K_w]or keys[pygame.K_UP]:
			jump = True;
	else:
		if jumpCount >= -10:
			y -= (jumpCount * abs(jumpCount)) * .4
			jumpCount -= 1
		else:
			jumpCount = 10
			jump = False
	win.fill((0,0,0))
	pygame.draw.rect(win, (255,0,0), (x, y, width, height))
	pygame.display.update()
    
pygame.quit()
"""

""" Player Movement Jumping using class
player = characters(50, 50, 500/2, 500/2, 10, False, 10)
while run:
	clock.tick(30)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	keys = pygame.key.get_pressed()
	if keys[pygame.K_a]:
		player.x -= player.speed

	if keys[pygame.K_d]:
		player.x += player.speed
	if not(player.jump):
		if keys[pygame.K_w]or keys[pygame.K_UP]:
			player.jump = True;
	else:
		if player.jumpCount >= -10:
			player.y -= (player.jumpCount * abs(player.jumpCount)) * .4
			player.jumpCount -= 1
		else:
			player.jumpCount = 10
			player.jump = False
	win.fill((0,0,0))
	pygame.draw.rect(win, (255,0,0), (player.x, player.y, player.width, player.height))
	pygame.display.update()
    
pygame.quit()
"""