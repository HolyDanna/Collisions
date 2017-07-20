import pygame

class AABB(object):
    def __init__(self, x, y, width, height, color = (255, 255, 255)):
        super(AABB, self).__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.corners = [[x, y],[x+width, y],[x+width, y+height],[x, y+height]]
        self.color = color
    def getCorners(self):
        return self.corners
    def render(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
    def move(self, x, y):
        self.x = self.x + x
        self.y = self.y + y
        self.corners = [[p[0]+x,p[1]+y] for p in self.corners]
    def getType(self):
        return "AABB"
    def project(self, vector):
        minP = vector[0]*self.corners[0][0]+vector[1]*self.corners[0][1]
        maxP = vector[0]*self.corners[0][0]+vector[1]*self.corners[0][1]
        for corner in self.corners:
            temp = vector[0]*corner[0]+vector[1]*corner[1]
            if temp < minP:
                minP = temp
            elif temp > maxP:
                maxP = temp
        return (minP, maxP)
    def getAxes(self):
        return [[1,0], [0,1]]
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
