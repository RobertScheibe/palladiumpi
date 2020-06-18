#!/usr/bin/python3

import inputs,os,pygame

print(inputs.devices.gamepads)

pads = inputs.devices.gamepads
select=0
start=0
disable_pad=False

pygame.init()
enable=pygame.mixer.Sound('enable.wav')
disable=pygame.mixer.Sound('disable.wav')

while True:
    events = inputs.get_gamepad()
    for event in events:
        #print(event.ev_type, event.code, event.state)
        if event.code == 'ABS_Y' and event.state == 255:
            #print("down")
            if not disable_pad:
                os.system("xte 'key Down'")
        elif event.code == 'ABS_Y' and event.state == 0:
            #print("up")
            if not disable_pad:
                os.system("xte 'key Up'")
        elif event.code == 'ABS_X' and event.state == 255:
            #print("right")
            if not disable_pad:
                os.system("xte 'key Right'")
        elif event.code == 'ABS_X' and event.state == 0:
            #print("left")
            if not disable_pad:
                os.system("xte 'key Left'")
        elif event.code == 'BTN_TRIGGER' and event.state == 1:
            #print("B")
            if not disable_pad:
                os.system("xte 'key Escape'")
            start=1
        elif event.code == 'BTN_TRIGGER' and event.state == 0:
            #print("B")
            start=0
        elif event.code == 'BTN_THUMB' and event.state == 1:
            #print("A")
            if not disable_pad:
                os.system("xte 'key Return'")
            select=1
        elif event.code == 'BTN_THUMB' and event.state == 0:
            #print("select")
            select=0
        elif event.code == 'BTN_BASE3' and event.state == 1:
            #print("select")
            if not disable_pad:
                os.system("xte 'keydown Meta_L' 'key F4' 'keyup Meta_L'")
        elif event.code == 'BTN_BASE4' and event.state == 1:
            #print("start")
            if not disable_pad:
                os.system("xte 'key Super_L'")
        if start == 1 and select == 1:
            print("toggle disable pad")
            disable_pad=not disable_pad
            if disable_pad:
                disable.play()
            else:
                enable.play()
            select=0
            start=0

