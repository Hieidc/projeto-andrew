import pyautogui
import pyperclip

email = pyautogui.prompt(text='Qual o seu email?', title='Pergunta')
senha = pyautogui.password(text='Digite sua senha', title='Senha do sistema', mask='*')

pyautogui.click(1155,194,duration=1)
pyautogui.typewrite(email)
pyautogui.press('enter')
pyautogui.typewrite(senha)