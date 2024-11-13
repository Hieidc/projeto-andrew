import pyautogui

#click personalizado
pyautogui.click(x=1486,y=541,clicks=2,interval=0.5, button='left',duration=2)

#click na posicao atual
pyautogui.click()
pyautogui.click(button='left')
pyautogui.click(button='right')
pyautogui.click(button='middle')
#clique x vezes
pyautogui.click(clicks=10)
#funcoes prontas
pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.middleClick()
pyautogui.tripleClick()