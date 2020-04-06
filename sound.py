import sys, pygame, math
pygame.init()

size = width, height = 1280, 720
black = 0, 0, 0
white = 255, 255, 255
speed = 0.2
rects = []

rects.append(pygame.Rect(0, 0, width, 5))
rects.append(pygame.Rect(0, 0, 5, height))
rects.append(pygame.Rect(width, 0, 5, height))

rects.append(pygame.Rect(400, 200, 100, 100))

def collides(point):
    for rect in rects:
        if rect.collidepoint(point):
            if abs(point[0] - rect.x) < abs(point[1] - rect.y):
                return "y"
            else:
                return "x"

    return ""

class Point(object):
    def __init__(self, position, direction):
        self.pos = position
        self.dir = direction

    def move(self):
        if collides(self.pos) == "x":
            self.dir[0] = -self.dir[0]
            self.dir[1] = -self.dir[1]
        elif collides(self.pos) == "y":
            self.dir[1] = -self.dir[1]
            self.dir[0] = -self.dir[0]



        self.pos[0] += self.dir[0] * speed
        self.pos[1] += self.dir[1] * speed

    def get_int_pos(self):
        return (int(self.pos[0]), int(self.pos[1]))


screen = pygame.display.set_mode(size)

points = []

n = 5000
for i in range(0, n):
    angle = i / n * 2 * math.pi
    points.append(Point([640, 360], [math.cos(angle), math.sin(angle)]))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed *= 1.5
            if event.key == pygame.K_DOWN:
                speed /= 1.5


    screen.fill(black)

    raw_points = []

    for point in points:
        point.move();
        raw_points.append(point.pos)
        screen.set_at(point.get_int_pos(), white)

    for rect in rects:
        pygame.draw.rect(screen, white, rect, 1)

    #pygame.draw.lines(screen, white, True, raw_points)

    pygame.display.flip()
