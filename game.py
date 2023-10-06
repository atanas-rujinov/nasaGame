import pygame
import random
import re
import time

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen2 = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Titan City")

#define 100x100 grid
grid = [[0 for x in range(10)] for y in range(10)]

class Building:
    def __init__(self, name, cost, income, incomeType, usedEnergy, usedResources, usedFood, usedResearch):
        self.name = name
        self.cost = cost
        self.usedResources = usedResources
        self.usedEnergy = usedEnergy
        self.usedFood = usedFood
        self.usedResearch = usedResearch
        self.income = income
        self.incomeType = incomeType # energy , resources , food , research


buildings = {
    1: Building("Main base", 0, 1, "research", 1, 1, 1, 1),

    2: Building("Methane extraction facility", 100, 10, "resources", 5, 1, 5, 5),
    3: Building("Research lab", 100, 10, "research", 5, 5, 5, 1),
    4: Building("Solar panels", 100, 10, "energy", 1, 5, 5, 5),
    5: Building("Hydroponics farm", 100, 10, "food", 5, 5, 1, 5),

    6: Building("Mining rig", 150, 20, "resources", 10, 1, 10, 10),
    7: Building("Communication array", 150, 20, "research", 10, 10, 10, 1),
    8: Building("Fuel refinery", 150, 20, "energy", 1, 10, 10, 10),
    9: Building("Fish farm", 150, 20, "food", 10, 10, 1, 10),
}

money = 100
resources = 100
energy = 100
food = 100
research = 100

timestamp = time.time()

sidebarPage = 1

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            if sidebarPage!=1 and mousePos[0] > 40 and mousePos[0] < 80 and mousePos[1] > 955 and mousePos[1] < 995:
                sidebarPage-=1
            elif sidebarPage!=2 and mousePos[0] > 120 and mousePos[0] < 160 and mousePos[1] > 955 and mousePos[1] < 995:
                sidebarPage+=1


    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 200, 1000))
    
    #draw grid
    for x in range(10):
        for y in range(10):
            pygame.draw.rect(screen, (255, 255, 255), (x*100+200, y*100, 100, 100), 1)  #to be rmoved
            pygame.draw.rect(screen, (grid[x][y]*25, 0, 0), (x*100+200, y*100, 99, 99)) #to be switched to 100
    grid[4][4] = 1
    
    if ((time.time() - timestamp) > 5):
        #calvculating income
        for x in range(10):
            for y in range(10):
                if grid[x][y] != 0:
                    if buildings[grid[x][y]].incomeType == "resources":
                        resources += buildings[grid[x][y]].income
                    elif buildings[grid[x][y]].incomeType == "energy":
                        energy += buildings[grid[x][y]].income
                    elif buildings[grid[x][y]].incomeType == "food":
                        food += buildings[grid[x][y]].income
                    elif buildings[grid[x][y]].incomeType == "research":
                        research += buildings[grid[x][y]].income
        timestamp = time.time()

        print("\n\nMoney: " + str(money))
        print("Resources: " + str(resources))
        print("Energy: " + str(energy))
        print("Food: " + str(food))
        print("Research:" + str(research))

    #drawing buldings to buy in the side bar
    if sidebarPage == 1:
        for x in range(5):
            pygame.draw.rect(screen, (0, 0, 0), (10, 5 + x*190, 180, 180))
    elif sidebarPage == 2:
        for x in range(3):
            pygame.draw.rect(screen, (0, 0, 0), (10, 5 + x*190, 180, 180))
    
    #draw page buttons
    if sidebarPage != 1:
        pygame.draw.rect(screen, (100, 100, 100), (40, 955, 40, 40))
        pygame.draw.polygon(screen, (0,0,0), ((40, 995), (80, 995), (60, 955)))
    #second triangle upside down
    if sidebarPage != 2:
        pygame.draw.rect(screen, (100, 100, 100), (120, 955, 40, 40))
        pygame.draw.polygon(screen, (0,0,0), ((120, 955), (160, 955), (140, 995)))


    pygame.display.flip()