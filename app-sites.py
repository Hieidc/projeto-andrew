#Automação de sites com PyAutoGUI
import pyautogui
import webbrowser
from time import sleep

#webbrowser.open('https://cursoautomacao.netlify.app/')
webbrowser.open_new('https://cursoautomacao.netlify.app/')
sleep(2)
#rolar pagina
pyautogui.moveTo(1224,221, duration=1)
pyautogui.scroll(-400)

#Digitar nome
#pyautogui.click(1493,800, duration=1)
digite_seu_nome = pyautogui.locateCenterOnScreen('nome.png')
pyautogui.click(digite_seu_nome[0],digite_seu_nome[1], duration=1)
pyautogui.typewrite('Andrew Kerscher')
alerta = pyautogui.locateCenterOnScreen('alerta.png')
pyautogui.click(alerta[0],alerta[1], duration=1)
sleep(1)
#Fechar alerta
pyautogui.click(1151,158, duration=1)
#pyautogui.locateCenterOnScreen('fechar1.png')
sleep(1)

#Subir barra de rolagem
pyautogui.scroll(400)
sleep(1)

#Descer até o download
pyautogui.scroll(-1500)

#Clicar no botão de download
excel = pyautogui.locateCenterOnScreen('excel.png')
pyautogui.moveTo(excel[0],excel[1], duration=1)
pyautogui.move(0,40, duration=1)
pyautogui.click()
#pyautogui.click(493,744, duration=1)
sleep(1)
pdf = pyautogui.locateCenterOnScreen('pdf.png')
pyautogui.click(pdf[0],pdf[1], duration=1)
pyautogui.move(0,40, duration=1)
pyautogui.click()
#pyautogui.click(679,746, duration=1)
sleep(1)

#Fechar navegador
pyautogui.alert(text='VOCÊ TERMINOU', title='Aviso')