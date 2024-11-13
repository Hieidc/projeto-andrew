import pyautogui
from time import sleep

#Navegar e clicar no campo e-mail:
pyautogui.click(1411,265,duration=2)
sleep(1)
#Digitar e-mail:
pyautogui.typewrite('e-mail@email.com')
sleep(1)
#apertar tab
pyautogui.press('tab')
sleep(1)
#Digitar senha
pyautogui.typewrite('123456')
sleep(1)
#apertar tab
pyautogui.press('tab')
sleep(1)
#aperta space
pyautogui.press('space')
sleep(1)

#para ver todas teclas possiveis
print(pyautogui.KEYBOARD_KEYS)

#Teclas de atalho + combinaçãos
pyautogui.keyDown('crtl')
pyautogui.keyDown('a')
pyautogui.keyUp('crtl')
pyautogui.keyUpn('a')

#ou 

pyautogui.hotkey('crtl','a')
