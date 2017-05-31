# !/usr/bin/python
# -*- coding: UTF-8 -*-

import pyautogui,time
width, height = pyautogui.size()

def moveMouse():
    """
    
    
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
    :return: 
    """
    pyautogui.moveRel(None, 2)


print('Press Ctrl-C to quit.')
try:
    index = 0
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        time.sleep(10)
        x_2, y_2 = pyautogui.position()
        if x == x_2 and y == y_2:
            index = index+1
        print(index)
        if index == 4:
            index = 0
            moveMouse()
        #print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone.')