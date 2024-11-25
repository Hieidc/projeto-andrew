import pyautogui
from time import sleep
import webbrowser


pyautogui.useImageNotFoundException(False)

def logoff():
    pyautogui.click(198,806, duration=1)
    pyautogui.click(79,996, duration=1)
    pyautogui.click(92,935, duration=1)
    

while True:
    #Acessar o instagram
    webbrowser.open_new('https://www.instagram.com')
    sleep(1)

    #email = pyautogui.prompt(text='Qual o seu email?', title='Pergunta')
    #senha = pyautogui.password(text='Digite sua senha', title='Senha do sistema', mask='*')

    #Digitar e-mail
    pyautogui.click(1163,369, duration=1)
    pyautogui.typewrite('cleverctb@hotmail.com')
    pyautogui.move(0,40, duration=1)
    pyautogui.click()
    pyautogui.typewrite('esposa512')
    pyautogui.move(0,45, duration=1)
    pyautogui.click()
    sleep(5)
    pyautogui.click(1100,624, duration=1)
    sleep(5)

    #Acessar perfil
    pyautogui.click(122,286, duration=1)
    sleep(2)
    pyautogui.click(350,220, duration=1)
    sleep(2)
    pyautogui.typewrite('nike')
    sleep(3)
    pyautogui.click(209,269, duration=1)
    sleep(2)

    #Acessar post
    pyautogui.click(784,700, duration=1)
    sleep(5)

    coracao = pyautogui.locateCenterOnScreen('coracao.png')
    #coracao1 = pyautogui.locateCenterOnScreen('coracao1.png')

    if coracao is not None:
        logoff()
        sleep(30)
    #elif coracao == None:
    else:
        pyautogui.click(1001,883, duration=1)
        sleep(2)
        pyautogui.click(1041,886, duration=1)
        sleep(2)
        pyautogui.click(1052,993, duration=1)
        sleep(1)
        pyautogui.typewrite('Show')
        sleep(1)
        pyautogui.click(1431,991,duration=1)
        sleep(5)
        logoff()
        sleep(30)