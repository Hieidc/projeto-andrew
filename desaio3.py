import pyautogui
import keyboard
import win32api
import win32con
from time import sleep

pyautogui.click(1547,442,duration=0.1)
#Posicao do mouse
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
#Clicar
while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(1440,474,(0,0,0)):
        click(1440,474)
        sleep(0.05)
    if pyautogui.pixelMatchesColor(1515,475,(0,0,0)):
        click(1515,475)
        sleep(0.05)
    if pyautogui.pixelMatchesColor(1592,471,(0,0,0)):
        click(1592,471)
        sleep(0.05)
    if pyautogui.pixelMatchesColor(1662,473,(0,0,0)):
        click(1662,473)        
        sleep(0.05)