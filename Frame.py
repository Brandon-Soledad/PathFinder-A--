import pygame
import sys
from Queue import PriorityQueue

def createGrid():
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    WHITE = (255,255,255)

    pygame.init()
    frame = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("PathFinder")
    frame.fill(WHITE)

    gameExit = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

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
        startState = State_String(self.start, 0, self.start, self.goal, self)
        count = 0
        self.priorityQueue.put((0, count, startState))
        while(not self.path and self.priorityQueue.qsize():
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