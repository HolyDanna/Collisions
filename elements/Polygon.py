import pygame

class Polygon(object):
    def __init__(self, points, color = (255, 255, 255)):
        super(Polygon, self).__init__()
        self.corners = points
        self.color = color
    def getCorners(self):
        return self.corners
    def render(self, surface):
        pygame.draw.polygon(surface, self.color, self.corners)
    def move(self, x, y):
        self.corners = [[p[0]+x,p[1]+y] for p in self.corners]
    def getType(self):
        return "polygon"
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
        c = self.corners
        l = len(c)
        axes = [[c[(i+1)%l][1]-c[1][1],c[1][0]-c[(i+1)%l][0]] for i in range(l)]
        return axes
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
