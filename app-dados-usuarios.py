#Alerta e pedir informacao
import pyautogui
import pyperclip
import time

# pyautogui.alert(text='Programa iniciado', title='Aviso', button='OK')

# #Pedir informação
# nome = pyautogui.prompt(text='Qual o seu nome?', title='Pergunta', default='Andrew')
# idade = pyautogui.prompt(text='Qual a sua idade?', title='Pergunta', default='0')
# print(f'Seu nome é {nome} e tem {idade} anos')
#Confirmar se algo deve ou nao acontecer

# resposta = pyautogui.confirm(text='Continuar rodando a automação',title='confirmar',buttons=['Sim','Não','Cancelar'])
# #print(resposta)
# if resposta == 'Sim':
#     print('Rodando a automação')
# elif resposta == 'Não':
#     print('Encerrando a automação')
# else:
#     print('Operação cancelada')


senha = pyautogui.password(text='Digite sua senha', title='Senha do sistema', mask='*')
print(senha)