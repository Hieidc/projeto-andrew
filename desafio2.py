import pyautogui
import keyboard
from time import sleep

while keyboard.is_pressed('1') == False:
    #Verificar a cor dos botoes 
    if pyautogui.pixelMatchesColor(792,795,(12,152,33)): #Verde
        pyautogui.press('a')
        sleep(0.1) 
    if pyautogui.pixelMatchesColor(880,798,(214,15,23)):  #Vermelho
        pyautogui.press('s')
        sleep(0.1) 
    if pyautogui.pixelMatchesColor(971,797,(244,244,64)): #Amarelo
        pyautogui.press('j')
        sleep(0.1) 
    if pyautogui.pixelMatchesColor(1059,799,(0,130,218)): #Azul
        pyautogui.press('k') 
        sleep(0.1) 
    if pyautogui.pixelMatchesColor(1150,799,(12,152,33)): #Laranja
        pyautogui.press('l')
        sleep(0.1) 