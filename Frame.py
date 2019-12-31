import pygame
import sys
from pynput.mouse import Button, Controller
from queue import PriorityQueue


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BLOCK_SIZE = 32
WHITE = (255,255,255)
RECT_COLOR = (0,0,15)
NEW_COLOR = (20,0,200)

pygame.init()

frame = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PathFinder")

# create list with all rects
all_rects = []
for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
    row = []
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        rect = pygame.Rect(x, y, BLOCK_SIZE-1, BLOCK_SIZE-1)
        row.append([rect, RECT_COLOR])            
    all_rects.append(row)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # check which rect was clicked and change its color on list
            for row in all_rects:
                for item in row:
                    rect, color = item
                    if rect.collidepoint(event.pos):
                        if color == RECT_COLOR:
                            item[1] = NEW_COLOR
                        else:
                            item[1] = RECT_COLOR

    # draw all in every loop

    frame.fill(WHITE)

    for row in all_rects:
        for item in row:
            rect, color = item
            pygame.draw.rect(frame, color, rect)

    pygame.display.flip()

def main():
    createGrid()

class Node(object):
    def __init__(self, value, parent, start = 0, goal = 0):
        self.children = []
        self.parent = parent
        self.value = value
        self.distance = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [value]
            self.start = start
            self.goal = goal
        def GetDistance(self):
            pass
        def CreateChildren(self):
            pass
class State_String(Node):
    def __init__(self, value, parent, start = 0, goal = 0):
        super(State_String, self).__init__(value
        , parent, start, goal)
        self.distance = self.getDistance()

        def GetDistance(self):
            if self.value == self.goal:
                return 0
            distance = 0
            for i in range(len(self.goal)):
                letter = self.goal[i]
                distance += abs(i - self.value.index(letter))
            return distance
        def CreateChildren(self):
            if not self.children:
                for i in xrange(len(self.goal)-1):
                    val = self.value
                    val = val[:i] + val[i+1] + val[i] + val[i+2]
                    child = State_String(val, self)
                    self.children.append(child)
class AStar:
    def __init__(self, start, goal):
        self.path = []
        self.VisitedQueue = []
        self.priorityQueue = PriorityQueue()
        self.start = start
    def Solve(self):
        startState = State_String(self.start, 0, self.start, self.goal)
        count = 0
        self.priorityQueue.put((0, count, startState))
        while(not self.path and self.priorityQueue.qsize()):
            closestChild = self.priorityQueue.get()[2]
            closestChild.CreateChildren()
            self.VisitedQueue.append(closestChild.value)
            for child in closestChild.children:
                if child.value not in self.VisitedQueue:
                    count += 1
                    if not child.distance:
                        self.path = child.path
                        break
                    self.priorityQueue.put(child.distance, count, child)
        if not self.path:
            print('Goal of' + self.goal + 'is not possible')
        return self.path


if __name__ == '__main__':
    main()    