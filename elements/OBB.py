import pygame

class OBB(object):
    def __init__(self, x, y, vector1, vector2, color = (255, 255, 255)):
        super(OBB, self).__init__()
        if (vector1[0]*vector2[0]+ vector1[1]*vector2[1] != 0):
            print("The two vector must be perpendicular !")
        else:
            self.x = x
            self.y = y
            self.vector1 = vector1
            self.vector2 = vector2
            self.corners = [[x,y], [x+vector1[0], y+vector1[1]], [x+vector1[0]+vector2[0], y+vector1[1]+vector2[1]], [x+vector2[0], y+vector2[1]]]
            self.color = color
    def getCorners(self):
        return self.corners
    def render(self, surface):
        pygame.draw.polygon(surface, self.color, self.corners)
    def move(self, x, y):
        self.x = self.x + x
        self.y = self.y + y
        self.corners = [[p[0]+x,p[1]+y] for p in self.corners]
    def getType(self):
        return "OBB"
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
        return [self.vector1, self.vector2]
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
