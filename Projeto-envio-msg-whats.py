# Automatizar whatsapp
import webbrowser
import pyautogui
from time import sleep


telefones = []
# Abrir arquivo txt
with open('fones.txt', 'r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.strip())

# Enviar as mensagens para os telefones
for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(20)
    pyautogui.click(959, 365, duration=1)
    sleep(10)
    pyautogui.click(950, 429, duration=1)
    sleep(10)
    pyautogui.typewrite('Ola, tudo bem? Teste de envio de msg pelo python')
    sleep(5)
    pyautogui.press('enter')
    pyautogui.click(1901,14, duration=1) #Fechar aba browser
    sleep(200)
