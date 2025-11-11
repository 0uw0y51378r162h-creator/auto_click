from time import sleep
import pyautogui
import numpy as np

def step(k):
    pyautogui.moveTo(952,399)
    pyautogui.click()
    for i in range(k):
        pyautogui.click()
        sleep(1)
    pyautogui.moveTo(914,795)
    pyautogui.click()
    sleep(1)
    pyautogui.moveTo(543,547)
    pyautogui.click()
    sleep(1)
    pyautogui.moveTo(297,603)
    n=0
    while True:
        pyautogui.click()
        n+=1
        sleep(3)
        if n>=60:
            pyautogui.moveTo(923,776)
            pyautogui.click()
            sleep(1)
            pyautogui.moveTo(543,547)
            pyautogui.click()
            break
    for x in range(5):
        pyautogui.moveTo(247,361)#選択肢
        sleep(1)
        pyautogui.click()#選択肢クリック
        sleep(1)
        pyautogui.moveTo(956,429)#answer
        sleep(1)
        pyautogui.doubleClick()#ans・NEXTクリック
        sleep(1)

step(5)