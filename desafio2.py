import pyautogui
import keyboard
from time import sleep

while keyboard.is_pressed('1') == False:
    #Verificar a cor dos botoes 
    if pyautogui.pixelMatchesColor(1396,821,(0,152,0)): #Verde
        pyautogui.press('a')
        sleep(0.05) 
    if pyautogui.pixelMatchesColor(1488,820,(255,0,0)):  #Vermelho
        pyautogui.press('s')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(1578,820,(244,244,2)): #Amarelo
        pyautogui.press('j')
        sleep(0.05) 