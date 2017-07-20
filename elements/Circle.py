import pygame

class Circle(object):
    """docstring for Circle."""
    def __init__(self, x, y, radius, color = (255, 255, 255), width = None):
        super(Circle, self).__init__()
        self.x = x
        self.y = y
        self.radius = radius
        if width is not None:
            self.width = width
        else:
            self.width = radius
        self.color = color
    def getCenter(self):
        return (self.x, self.y)
    def getRadius(self):
        return self.radius
    def render(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius, self.width)
    def move(self, x, y):
        self.x = self.x + x
        self.y = self.y + y
    def getType(self):
        return "Circle"
    def project(self, vector):
        minP = vector[0]*self.x+vector[1]*self.y
        maxP = vector[0]*self.x+vector[1]*self.y
        minP = minP - self.radius*(vector[0]**2 + vector[1]**2)**0.5
        maxP = maxP + self.radius*(vector[0]**2 + vector[1]**2)**0.5
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
