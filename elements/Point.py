import pygame

class Point(object):
    """docstring for Circle."""
    def __init__(self, x, y, color = (255, 255, 255)):
        super(Point, self).__init__()
        self.x = x
        self.y = y
        self.color = color
    def getCoordinates(self):
        return (self.x, self.y)
    def render(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), 1, 0)
    def move(self, x, y):
        self.x = self.x + x
        self.y = self.y + y
    def getType(self):
        return "Point"
    def project(self, vector):
        minP = vector[0]*self.x+vector[1]*self.y
        maxP = vector[0]*self.x+vector[1]*self.y
        minP = minP - 1*(vector[0]**2 + vector[1]**2)**0.5
        maxP = maxP + 1*(vector[0]**2 + vector[1]**2)**0.5
        return (minP, maxP)
    def getAxes(self):
        return []
    def update(self, keys):
        refreshNeeded = False
        if (keys[pygame.K_UP]):
            self.move(0,-1)
            refreshNeeded = True
        if (keys[pygame.K_DOWN]):
            self.move(0,1)
            refreshNeeded = True
        if (keys[pygame.K_LEFT]):
            self.move(-1,0)
            refreshNeeded = True
        if (keys[pygame.K_RIGHT]):
            self.move(1,0)
            refreshNeeded = True
        return refreshNeeded
