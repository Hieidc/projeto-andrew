import pyautogui
import pyperclip #Para utilizar caracteres especiais
#from time import sleep

pyautogui.click(1208,241,duration=0.5)

#sleep(1)

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('Ctrl','v')

escrever_frase('Automação é Incrível!')