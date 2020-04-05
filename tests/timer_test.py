import pygame

pygame.init()

my_event = 8
pygame.time.set_timer(my_event, 6000)

iters = 0
while True:
    for event in pygame.event.get():
        print(event)
    if iters >= 7:
        my_event = 9
    print(my_event)
    iters += 1
    pygame.time.delay(500)