# -*- coding = utf-8 -*-

import cv2
from PIL import ImageGrab
import time
from time import sleep
from mss import mss
from PIL import Image
import pyautogui as pg
import random


template1 = cv2.imread('guang130.png')
template2 = cv2.imread('guang100.png')
template3 = cv2.imread('an130.png')
template4 = cv2.imread('feng130.png')
template5 = cv2.imread('shui130.png')
template6 = cv2.imread('huo130.png')
template7 = cv2.imread('lei130.png')
template8 = cv2.imread('huan110.png')
template16 = cv2.imread('jiuyuan.png')  # 救援
template17 = cv2.imread('huanshou.png')  # 幻兽
template18 = cv2.imread('queren.png')  # 奖励确认
template19 = cv2.imread('OK.png')  # boss死了
template20 = cv2.imread('die.png')  # 我死了
# cv2.imshow("Image", image)
# cv2.imshow("Template", template)
# 将图像和模板都转换为灰度
templateGray1 = cv2.cvtColor(template1, cv2.COLOR_BGR2GRAY)
templateGray2 = cv2.cvtColor(template2, cv2.COLOR_BGR2GRAY)
templateGray3 = cv2.cvtColor(template3, cv2.COLOR_BGR2GRAY)
templateGray4 = cv2.cvtColor(template4, cv2.COLOR_BGR2GRAY)
templateGray5 = cv2.cvtColor(template5, cv2.COLOR_BGR2GRAY)
templateGray6 = cv2.cvtColor(template6, cv2.COLOR_BGR2GRAY)
templateGray7 = cv2.cvtColor(template7, cv2.COLOR_BGR2GRAY)
templateGray8 = cv2.cvtColor(template8, cv2.COLOR_BGR2GRAY)
templateGray16 = cv2.cvtColor(template16, cv2.COLOR_BGR2GRAY)
templateGray17 = cv2.cvtColor(template17, cv2.COLOR_BGR2GRAY)
templateGray18 = cv2.cvtColor(template18, cv2.COLOR_BGR2GRAY)
templateGray19 = cv2.cvtColor(template19, cv2.COLOR_BGR2GRAY)
templateGray20 = cv2.cvtColor(template20, cv2.COLOR_BGR2GRAY)

list = [templateGray1,templateGray2,templateGray3,templateGray4,templateGray5,templateGray6,templateGray7,templateGray8]
list1 = [template1,template2,template3,template4,template5,template6,template7,template8]

imageGray = 0
image = 0


def move_random(x_end,y_end,step_p):
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


def capture_screenshot():
    # Capture entire screen
    with mss() as sct:
        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)
        # Convert to PIL/Pillow Image
        return Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')


def ncc_huanshou():
    global imageGray
    global image
    img = capture_screenshot()
    img.save('screenshot.png')
    # 从磁盘加载输入图像和模板图像，然后显示在我们的屏幕上
    image = cv2.imread('screenshot.png')
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(imageGray, templateGray17, cv2.TM_CCOEFF_NORMED)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
    if maxVal > 0.9:
        (startX, startY) = maxLoc
        endX = startX + template17.shape[1]
        endY = startY + template17.shape[0]
        midX = (startX + endX) / 2
        midY = (startY + endY) / 2

        move_random(midX+400+random.randint(0,4), midY+random.randint(0,4), 1)  # 点击幻兽
        sleep(1)
        pg.click()
    else:
        move_random(2429+random.randint(0,4), 912+random.randint(0,4), 1)  # 点击第三只幻兽
        sleep(1)
        pg.click()


def ncc_jiuyuan():
    global imageGray
    global image
    img = capture_screenshot()
    img.save('screenshot.png')
    # 从磁盘加载输入图像和模板图像，然后显示在我们的屏幕上
    image = cv2.imread('screenshot.png')
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(imageGray, templateGray16, cv2.TM_CCOEFF_NORMED)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
    if maxVal > 0.9:
        move_random(2700+random.randint(0,4), 900+random.randint(0,4), 1)  # 救援
        pg.click()
        sleep(1)
    else:
        sleep(3)
        ncc_jiuyuan()


def ncc_end():
    global imageGray
    global image
    img = capture_screenshot()
    img.save('screenshot.png')
    # 从磁盘加载输入图像和模板图像，然后显示在我们的屏幕上
    image = cv2.imread('screenshot.png')
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(imageGray, templateGray19, cv2.TM_CCOEFF_NORMED)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
    if maxVal > 0.9:
        (startX, startY) = maxLoc
        endX = startX + template19.shape[1]
        endY = startY + template19.shape[0]
        midX = (startX + endX) / 2
        midY = (startY + endY) / 2

        move_random(midX+random.randint(0,4), midY+random.randint(0,4), 1)  # 点击OK
        sleep(1)
        pg.click()
        move_random(2630+random.randint(0,4), 1000+random.randint(0,4), 1)  # 退出
        sleep(1)
        pg.click()
        return True


def ncc_die():
    global imageGray
    global image
    img = capture_screenshot()
    img.save('screenshot.png')
    # 从磁盘加载输入图像和模板图像，然后显示在我们的屏幕上
    image = cv2.imread('screenshot.png')
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(imageGray, templateGray20, cv2.TM_CCOEFF_NORMED)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
    if maxVal > 0.9:
        move_random(2560+random.randint(0,4), 860+random.randint(0,4), 1)
        sleep(1)
        pg.click()
        move_random(2440+random.randint(0,4), 670+random.randint(0,4), 1)
        sleep(1)
        pg.click()
        sleep(3)
        move_random(2930+random.randint(0,4), 700+random.randint(0,4), 1)  # 点击打车
        sleep(1)
        pg.click()
        return True



def maxVal_queren():
    result = cv2.matchTemplate(imageGray, templateGray18, cv2.TM_CCOEFF_NORMED)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
    if maxVal > 0.9:
        (startX, startY) = maxLoc
        endX = startX + template18.shape[1]
        endY = startY + template18.shape[0]
        midX = (startX + endX) / 2
        midY = (startY + endY) / 2

        move_random(midX+random.randint(0,4), midY+random.randint(0,4), 1)  # 点击奖励
        sleep(1)
        pg.click()
        move_random(2520+random.randint(0,4), 480+random.randint(0,4), 1)  # 点击第一个奖励
        sleep(1)
        pg.click()
        move_random(2570+random.randint(0,4), 920+random.randint(0,4), 1)  # OK
        sleep(7)
        pg.click()
        move_random(2630+random.randint(0,4), 1000+random.randint(0,4), 1)  # 退出
        sleep(1)
        pg.click()
        sleep(15)
        return True
    else:
        return False


def maxVal(num):
    # 执行模板匹配
    result = cv2.matchTemplate(imageGray, list[num-1], cv2.TM_CCOEFF_NORMED)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
    if maxVal > 0.9:
        (startX, startY) = maxLoc
        endX = startX + list1[num-1].shape[1]
        endY = startY + list1[num-1].shape[0]
        midX = (startX + endX) / 2
        midY = (startY + endY) / 2

        move_random(midX+random.randint(0,4), midY+random.randint(0,4), 1)  # 点击boss
        sleep(0.5)
        pg.click()
        sleep(2)
        ncc_huanshou()       # 助战界面
        sleep(1)
        move_random(2700+random.randint(0,4), 985+random.randint(0,4), 1)  # 确认
        sleep(0.5)
        pg.click()
        move_random(2700+random.randint(0,4), 800+random.randint(0,4), 1)  # 非有利属性提醒
        sleep(1)
        pg.click()
        sleep(15)
        move_random(2700+random.randint(0,4), 900+random.randint(0,4), 1)  # 救援
        pg.click()
        sleep(1)
        move_random(2770+random.randint(0,4), 950+random.randint(0,4), 1)  # 攻击
        sleep(0.3)
        pg.click()
        return True



def ncc():
    global imageGray
    global image
    img = capture_screenshot()
    img.save('screenshot.png')
    # 从磁盘加载输入图像和模板图像，然后显示在我们的屏幕上
    image = cv2.imread('screenshot.png')
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 确定起点和终点的（x，y）坐标边界框
    while not maxVal_queren():
        if maxVal(1):
            return True
        elif maxVal(2):
            return True
        elif maxVal(3):
            return True
        elif maxVal(4):
            return True
        elif maxVal(5):
            return True
        elif maxVal(6):
            return True
        elif maxVal(7):
            return True
        elif maxVal(8):
            return True
        else:
            return False

    # cv2.imshow("Output", image)
    cv2.waitKey(0)

def BP():
    move_random(2035+random.randint(0,4), 300+random.randint(0,4), 1) #回到主界面
    sleep(0.5)
    pg.click()
    move_random(2860, 314, 1) #AP加号
    sleep(0.5)
    pg.click()
    move_random(2715, 740, 1) #点击药瓶
    sleep(0.5)
    pg.click()
    move_random(2622, 933, 1) #拖动到数字
    sleep(0.5)
    pg.scroll(-1000)   #滚轮下滑到药瓶
    sleep(0.5)
    pg.click()
    move_random(2700+random.randint(0,4), 850+random.randint(0,4), 1)  # 确认使用BP
    sleep(0.5)
    pg.click()
    move_random(2575+random.randint(0,4), 808+random.randint(0,4), 1)  # OK
    sleep(0.5)
    pg.click()
    move_random(2930+random.randint(0,4), 700+random.randint(0,4), 1)  # 点击打车
    sleep(0.5)
    pg.click()
    sleep(2)


def refresh():
    move_random(1828, 76, 1)  # 刷新页面
    sleep(0.6)
    pg.click()
    sleep(30)
    move_random(1828, 76, 1)  # 刷新页面
    sleep(0.6)
    pg.click()
    move_random(2570+random.randint(0,4), 975+random.randint(0,4), 1)  # 点击进入
    sleep(20)
    pg.click()
    move_random(2930+random.randint(0,4), 700+random.randint(0,4), 1)  # 点击打车
    sleep(10)
    pg.click()

cnt = 1
cnt1 = 0
page = 1
move_random(2930+random.randint(0,4), 700+random.randint(0,4), 1)  # 点击打车
sleep(0.5)
pg.click()
while True:
    sleep(3)
    cnt1 = cnt1+1
    if cnt1 > 15 :
        cnt1 = 0
        refresh()
        print('refresh')
    if cnt % 13 == 0:
        cnt=cnt+1
        BP()
        print('BP')
    if ncc():
        cnt1 = 0
        page = 1
        cnt = cnt + 1
        print(cnt)
        for i in range(0,30):         # 30 = 15分钟 在打车时的最大等候时间，可根据自己多久死决定，要是不会死可以开很高
            sleep(30)           # 每30s检测BOSS
            if ncc_end():
                break
            elif ncc_die():
                break

    else:
        page = page + 1
        if page > 3:
            move_random(2035+random.randint(0,4), 300+random.randint(0,4), 1)  # 回到主界面
            sleep(1)
            pg.click()
            sleep(20)
            move_random(2930+random.randint(0,4), 700+random.randint(0,4), 1)  # 点击打车
            sleep(0.5)
            pg.click()
            page = 1
        else:
            move_random(2830+random.randint(0,4), 810+random.randint(0,4), 1)  # 翻页
            sleep(0.5)
            pg.click()


