import sys, pygame

pygame.init()
pygame.font.init()

global HOK_X
global HOK_Y
HOK_X = 34
HOK_Y = 23
KRAT_PAD = 12
KRAT_X = HOK_X * 6
KRAT_Y = HOK_Y * 5 + KRAT_PAD
NAME_X = 40

size = width, height = 1528, 1080
speed = [2, 2]
black = 0, 0, 0
grey  = 200, 200, 200
white = 255, 255, 255

font = pygame.font.SysFont('Ubuntu', 36)
small_font = pygame.font.SysFont('Ubuntu', 16)

screen = pygame.display.set_mode(size)

names = [["Dafne", "Pieter", "Bram", "Loes", "Huib", "Max"], ["Walter", "Rob", "Cas", "Daan", "Sophie", "Emilie"]]
# names = ["Walter", "Rob", "Cas", "Daan", "Sophie", "Emilie"]
for l in names:
    l.reverse()

logo = pygame.image.load("cpbw.png")
logo = pygame.transform.scale(logo, (250, 250))

namelist = 0

def draw_krat(posx, posy):
    for x in range(0, 6):
        for y in range (0, 4):
            pygame.draw.rect(screen, grey, pygame.Rect(posx + x * HOK_X, \
                posy + y * HOK_Y, HOK_X, HOK_Y / 2), 1)
            pygame.draw.rect(screen, black, pygame.Rect(posx + x * HOK_X, \
                posy + y * HOK_Y, HOK_X, HOK_Y), 1)

    for i in [1, 4]:
        pygame.draw.rect(screen, black, pygame.Rect(posx + i * HOK_X, \
            posy + 4 * HOK_Y + KRAT_PAD, HOK_X, HOK_Y), 2)


    pygame.draw.rect(screen, black, pygame.Rect(posx - 1, posy - 1, 6 * HOK_X, \
        4 * HOK_Y), 5)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            print(pygame.mouse.get_pos())
            pygame.image.save(screen, "screenshot" + str(namelist) + ".jpeg")
            namelist = (namelist + 1) % 2

    screen.fill(white)

    draw_krat(1750 - 4 * KRAT_X - 320, 2 * KRAT_PAD)
    draw_krat(1750 - 2 * KRAT_X - 320, 2 * KRAT_PAD)

    text = font.render("Gehaald:" + " " * 39 + "Terug:", True, black)
    screen.blit(text, (468, 50))

    for x in range(0, 6):
        for y in range(5, -1, -1):
            draw_krat((1500 - 6 * (KRAT_X + KRAT_PAD)) + x * (KRAT_X - 1),\
                 1060 - KRAT_Y - 1.5 * KRAT_PAD - y * (KRAT_Y + KRAT_PAD))
    c = 0
    for name in names[namelist]:
        c += 1
        text = font.render(name, True, (0, 0, 0))
        screen.blit(text, (NAME_X, 1060 - c * (KRAT_Y + KRAT_PAD)))

        statiegeld_text = small_font.render("Statiegeld:  x", True, black)
        screen.blit(statiegeld_text, (NAME_X, 1100 - c * (KRAT_Y + KRAT_PAD)))

    screen.blit(logo, pygame.Rect(20, 0, 250, 250))

    pygame.display.flip()
