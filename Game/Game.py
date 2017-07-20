import pygame
pygame.init()
from Game.collisions import *
from Game.Screen import *

class Game(object):
    def __init__(self, height = 450, width = 800):
        super(Game, self).__init__()
        self.selected_n = 0
        self.components = []
        self.selected = None
        self.Screen = Screen(height, width)
        self.clock = pygame.time.Clock()

    # getting the inputs
    def getInput(self):
        # this one is to prevent freezing from the pygame Windows
        pygame.event.get()
        # we return the list of currently pressed keys
        # we do not care about other input, in this 'game'
        return pygame.key.get_pressed()

    # now, let's update the game using our inputs
    def update(self, keys):
        # if the backspace key is pressed, we stop the game
        if (keys[pygame.K_BACKSPACE]):
            pygame.quit()
            return False
        # else we update the data for the selected element
        # we choose to only allow changes on the selected element, considering the others are static
        # if we were to allow changes to more elements, we would also need to update them
        # the value refreshNeeded tells us whether or not some elements have been moved
        refreshNeeded = self.selected.update(keys)
        # if the a (qwerty)/q(azerty) was pressed, we select the next element
        if (keys[pygame.K_a]):
            self.selected_n = (self.selected_n+1)%len(self.components)
            self.selected = self.components[self.selected_n]
        # we now chack for intersections if elements have been moved
        if refreshNeeded:
            checkCollisions(self.selected, self.components)
        # we return the result of our update : whether or not the screen needs to be refreshed
        return refreshNeeded

    # outputing what need to be output
    def output(self):
        surface = self.Screen.getSurface()
        # we reset was is printed on the surface
        self.Screen.render()
        for i in self.components:
            i.render(surface)

    def launch(self):
        gameRunning = True
        while gameRunning:
            self.clock.tick(60)
            # input part
            keys = self.getInput()
            # update part
            refresh = self.update(keys)
            if refresh:
                self.output()
            pygame.display.update()

    def add(self, component):
        self.components.append(component)
        self.selected = component
        self.selected_n = len(self.components)
