#!/usr/bin/python3

import pygame

pygame.display.init()
pygame.joystick.init()

print ("Joystics: ", pygame.joystick.get_count())
my_joystick = pygame.joystick.Joystick(0)
my_joystick.init()
clock = pygame.time.Clock()

print (my_joystick.get_numbuttons())
print (my_joystick.get_numhats())
while 1:
    for event in pygame.event.get():
        print (my_joystick.get_axis(0),  my_joystick.get_axis(1))
        for i in range(my_joystick.get_numbuttons()):
            print(i, my_joystick.get_button(i))
        clock.tick(40)

pygame.quit ()
