import pygame

class Screen(object):
    def __init__(self, height=450, width=800):
        super(Screen, self).__init__()
        self.height = height
        self.width = width
        self.surface = pygame.display.set_mode((self.width, self.height), 0, 32)
        self.color = (0,0,0)
    def getSurface(self):
        return self.surface
    def setWidth(self, width):
        self.width = width
        self.surface = pygame.display.set_mode((self.width, self.height), 0, 32)
    def getWidth(self):
        return self.width
    def setHeight(self, height):
        self.height = height
        self.surface = pygame.display.set_mode((self.width, self.height), 0, 32)
    def getHeight(self):
        return self.height
    def setColor(self, color):
        self.color = color
        self.render()
    def render(self):
        self.surface.fill(self.color)
