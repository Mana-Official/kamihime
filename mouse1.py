# -*- coding = utf-8 -*-
import random
import pyautogui as pg


def move_test(x_end,y_end,step_p):
    step = 40*step_p
    x, y = pg.position()
    for i in range(0, step):
        x1, y1 = pg.position()
        if i <= step / 2:
            dx = random.random() * (x_end - x) / step
            dy = random.random() * (y_end - y) / step
        else:
            dx = random.random() * (x_end - x) / step * 2
            dy = random.random() * (y_end - y) / step * 2
        pg.moveTo(x1+dx,y1+dy,random.random() * 0.05)
    pg.moveTo(x_end, y_end, 0.2)


