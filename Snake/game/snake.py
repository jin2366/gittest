import pygame

width = 500
height = 500
rows = 20


class Cube():
    def __init__(self, start, x=0, y=0, color=(255, 0, 0)):
        pass

    def move(self, x, y):
        pass

    def draw(self, surface, eyes=False):
        pass

class Snake():
    def __init__(self, color, pos):
        pass

    def move(self, pos):
        pass

    def addBody(self):
        pass

    def draw(self, surface):
        pass

window = pygame.display.set_mode((width, height))


def reDrawWindow():
    window.fill((0, 0, 0))
    drawGrid(width, rows, window)
    pygame.display.update()

def drawGrid(width, rows, surface):
    length = width // rows
    x = 0
    y = 0

    for i in range(rows):
        x = x + length
        y = y + length
        pygame.draw.line(surface, (128, 128, 128), (x, 0), (x, width))
        pygame.draw.line(surface, (128, 128, 128), (0, y), (width, y))


def randomFood(rows, food):
    pass

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();

        reDrawWindow()


main()
    


