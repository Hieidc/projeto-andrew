# Reconhecimento de imagem simples
import pyautogui

#print (pyautogui.locateOnScreen('numero_4.png'))
#Encontrar a coordenada do centro da imagem
#pyautogui.locateCenterOnScreen('numero_4.png')

captcha = pyautogui.locateCenterOnScreen('google.png')
pyautogui.click(captcha[0],captcha[1],duration=2)