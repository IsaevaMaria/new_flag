import pygame

pygame.init()
size = width, heigth = 300, 300
screen = pygame.display.set_mode(size)

def draw():
    rect_color = pygame.Color('brown')
    rect_width = 0
    rect_point = [[50,20], [5, 250]]
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)
    rect_color = pygame.Color('white')
    rect_width = 0
    rect_point = [[50, 30], [200, 50]]
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)

    rect_color = pygame.Color('blue')
    rect_width = 0
    rect_point = [[50, 70], [200, 50]]
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)
    rect_color = pygame.Color('red')
    rect_width = 0
    rect_point = [[50, 110], [200, 50]]
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)


draw()
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()